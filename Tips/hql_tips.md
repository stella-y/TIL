### random select
```sql
SELECT column FROM table ORDER BY RAND() LIMIT 1
```

### get row numbers
```sql
SELECT ROW_NUMBER() 
        OVER (ORDER BY EmployeeName) AS Row, 
    EmployeeId, EmployeeName, Salary 
FROM Employees
```

### shuffle rows
```sql
select * from user_stella.nmf_train_input
sort by rand()
```

### collect set (set 으로 묶기-WrappedArray)
```sql
select u, collect_set(i)
from user_stella.nmf_train_ui_vector
group by u
```

### replace
```sql
select Replace(Replace(Replace('2014/10/01 00:00:00', ' ', ''), ':', ''), '/', '')
from DUAL
-- 20141001000000
```
```sql
select Regexp_Replace('2014/10/01 00:00:00', ' |:|/', '')
from DUAL
-- 20141001000000
```

### session 분석
- request_timestamp가 epoch으로 남고, 30분 단위로 session을 나누고 싶은 경우
```sql
create table db.session_table as
select account_id, sum(new_event_boundary) over (PARTITION by account_id order by request_timestamp) as session_id,
request_timestamp,
minutes_since_last_interval,
new_event_boundary
from
(select account_id, request_timestamp, (request_timestamp-lag(request_timestamp)
	OVER (PARTITION BY account_id ORDER BY request_timestamp))/60000 as minutes_since_last_interval,
	case when request_timestamp-lag(request_timestamp) OVER (PARTITION BY account_id ORDER BY request_timestamp) > 30 * 60000 then 1 ELSE 0 END as new_event_boundary
from db.raw_data
where account_id is not null and account_id!=0) a
```
- 참고 : https://randyzwitch.com/sessionizing-log-data-sql/
