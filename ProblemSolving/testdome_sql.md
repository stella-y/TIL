1. Students
- problem
```
Given the following data definition, write a query that returns the number of students whose first name is John. String comparisons should be case sensitive.

TABLE students
   id INTEGER PRIMARY KEY,
   firstName VARCHAR(30) NOT NULL,
   lastName VARCHAR(30) NOT NULL
```
- solution
```sql
select count(*)
from students
where firstName='John'
```
2. Enrollment
- problem
```
A table containing the students enrolled in a yearly course has incorrect data in records with ids between 20 and 100 (inclusive).

TABLE enrollments
  id INTEGER NOT NULL PRIMARY KEY
  year INTEGER NOT NULL
  studentId INTEGER NOT NULL
Write a query that updates the field 'year' of every faulty record to 2015.
```
- solution
```sql
update enrollments set year=2015 where id >=20 and id <=100
```
3. Pets
- problem
```
Information about pets is kept in two separate tables:

TABLE dogs
  id INTEGER NOT NULL PRIMARY KEY,
  name VARCHAR(50) NOT NULL

TABLE cats
  id INTEGER NOT NULL PRIMARY KEY,
  name VARCHAR(50) NOT NULL
Write a query that select all distinct pet names.

See the example case for more details.
```
- solution
```sql
select name
from dogs
union
select name
from cats
```
4. Sessions
- problem
```
App usage data are kept in the following table:

TABLE sessions
  id INTEGER PRIMARY KEY,
  userId INTEGER NOT NULL,
  duration DECIMAL NOT NULL
Write a query that selects userId and average session duration for each user who has more than one session.

See the example case for more details.
```
- solution
```sql
select userId, avg(duration)
from sessions
group by userId
having count(userId)>1
```
5. Web Shop
- problem
```
Each item in a web shop belongs to a seller. To ensure service quality, each seller has a rating.

The data are kept in the following two tables:

TABLE sellers
  id INTEGER PRIMARY KEY,
  name VARCHAR(30) NOT NULL,
  rating INTEGER NOT NULL

TABLE items
  id INTEGER PRIMARY KEY,
  name VARCHAR(30) NOT NULL,
  sellerId INTEGER REFERENCES sellers(id)
Write a query that selects the item name and the name of its seller for each item that belongs to a seller with a rating greater than 4. The query should return the name of the item as the first column and name of the seller as the second column.

See the example case for more details.
```
- solution
```sql
select b.name, a.name
from
(select id, name
from sellers
where rating > 4) a
join
(select name, sellerId
from items) b
on a.id=b.sellerId

```
6. Workers
- problem
```
The following data definition defines an organization's employee hierarchy.

An employee is a manager if any other employee has their managerId set to this employee's id. That means John is a manager if at least one other employee has their managerId set to John's id.

TABLE employees
  id INTEGER NOT NULL PRIMARY KEY
  managerId INTEGER REFERENCES employees(id)
  name VARCHAR(30) NOT NULL
Write a query that selects the names of employees who are not managers.

See the example case for more details.
```
- solution
```sql
select a.name
from 
(select id, name
from employees) a
left join
(select managerId
 from employees
) b
on a.id=b.managerId
where managerId is Null
```
7. Users And RolesCONSTRAINTS
- problem
```
The following two tables are used to define users and their respective roles:

TABLE users
  id INTEGER NOT NULL PRIMARY KEY,
  userName VARCHAR(50) NOT NULL

TABLE roles
  id INTEGER NOT NULL PRIMARY KEY,
  role VARCHAR(20) NOT NULL
The users_roles table should contain the mapping between each user and their roles. Each user can have many roles, and each role can have many users.

Modify the provided SQLite create table statement so that:

Only users from the users table can exist within users_roles.
Only roles from the roles table can exist within users_roles.
A user can only have a specific role once.
See the example case for more details.
```
- solution
```sql
CREATE TABLE users_roles (
  userId INTEGER not null,
  roleId INTEGER not null,
  foreign key (userId) references users(id),
  foreign key (roleId) references roles(id),
  unique (userId, roleId)
);
```
8. Regional Sales Comparison
- problem
```
An insurance company maintains records of sales made by its employees. Each employee is assigned to a state. States are grouped under regions. The following tables contain the data:

TABLE regions
  id INTEGER PRIMARY KEY
  name VARCHAR(50) NOT NULL

TABLE states
  id INTEGER PRIMARY KEY
  name VARCHAR(50) NOT NULL
  regionId INTEGER NOT NULL REFERENCES regions(id)

TABLE employees
  id INTEGER PRIMARY KEY
  name VARCHAR(50) NOT NULL
  stateId INTEGER NOT NULL REFERENCES states(id)

TABLE sales
  id INTEGER PRIMARY KEY
  amount INTEGER NOT NULL
  employeeId INTEGER NOT NULL REFERENCES employees(id)  
Management requires a comparative region sales analysis report.
Write a query that returns:

The region name.
Average sales per employee for the region (Average sales = Total sales made for the region / Number of employees in the region).
The difference between the average sales of the region with the highest average sales, and the average sales per employee for the region (average sales to be calculated as explained above).
Employees can have multiple sales. A region with no sales should be also returned. Use 0 for average sales per employee for such a region when calculating the 2nd and the 3rd column.

See the example case for more details.
```
- solution
```sql
create table r_average as
select region_name, average
from
(
select r_name.name as region_name, coalesce(sum(s_total.total)/count(s_total.id), 0) as average
from 
(
	select s.id, r.name
	from 
	states s
	join
	regions r
	on (s.regionId=r.id)
) r_name
left join
(
	select e.id, e.stateId, coalesce(s.total, 0) as total
	from 
	employees e
	left join
	(
		select employeeId, count(*) as cnt, sum(amount) as total
		from sales
		group by employeeId
	) s
	on (e.id=s.employeeId)
) s_total
on (s_total.stateId=r_name.id)
group by region_name
);

select region_name, average, (select max(average) from r_average)-average
from r_average;
```
