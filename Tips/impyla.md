## impyla
패키지 이름은 impyla 인데, 코드에서 호출(import)할때는 impala를 호출해야함
### impyla 통해 python 에서 hive server2 접근하기
```python
from impala.dbapi import connect
conn=connect(host='[하이브 서버주소]',
             port=10000, #커버로스 인증 필요하다면 아래 과정 필요
             auth_mechanism='GSSAPI',
             kerberos_service_name='hive'
            )
cursor=conn.cursor()
cursor.execute("show databases")
result=cursor.fetchall()
print(result)
```
### fetchall 성능이 느린 경우
* sql 결과를 전부 다 메모리에 올리고 있으니 당연히 성능이슈...
* 뚜렷한 다른 방법이 있다기보단 쪼개서 가져오게 만들어서 그 batch 단위로 학습시키는게 최선일 듯
* 가져올 데이터를 임시테이블로 만들고, 거기서 몇개의 row 씩 가져오게 할지를 설정
```python
class CarbonHiveConn():
    def __init__(self):
        self.conn=connect(host='[하이브 서버주소]',
             port=10000,
             auth_mechanism='GSSAPI',
             kerberos_service_name='hive'
            )
        
        self.cursors = dict()
        
    def createTableUsingQuery(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        cursor.close()
    
    def setTableCursor(self, dbName, tableName):
        cursor = self.conn.cursor()
        cursor.execute("select * from " + dbName + "." + tableName)
        self.cursors[dbName + "." + tableName] = cursor
    
    def getTableData(self, dbName, tableName, count):
        return self.cursors[dbName + "." + tableName].fetchmany(count)

batch_size = 128
load_size = batch_size*1024

while True:
	dataSet = carbonHive.getTableData("임시 디비", "임시 테이블", load_size)
    rows = cursor.fetchmany(2)
    if not rows or len(rows)==0::
        break
    print(rows)
    procedData = toTensor(dataSet)
    dataloader = DataLoader(procedData, batch_size=batch_size, shuffle=True)
    # 이후 연산 쭉쭉...
```
참고 : https://community.cloudera.com/t5/Support-Questions/Impyla-bad-performance-rows-fetch-is-very-slow/td-p/87210
https://thepythonguru.com/fetching-records-using-fetchone-and-fetchmany/
