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
