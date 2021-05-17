Table: Sessions

+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| session_id          | int     |
| duration            | int     |
+---------------------+---------+
session_id is the primary key for this table.
duration is the time in seconds that a user has visited the application.
 

You want to know how long a user visits your application. You decided to create bins of "[0-5>", "[5-10>", "[10-15>" and "15 minutes or more" and count the number of sessions on it.

Write an SQL query to report the (bin, total) in any order.

The query result format is in the following example.

Sessions table:
+-------------+---------------+
| session_id  | duration      |
+-------------+---------------+
| 1           | 30            |
| 2           | 199           |
| 3           | 299           |
| 4           | 580           |
| 5           | 1000          |
+-------------+---------------+

Result table:
+--------------+--------------+
| bin          | total        |
+--------------+--------------+
| [0-5>        | 3            |
| [5-10>       | 1            |
| [10-15>      | 0            |
| 15 or more   | 1            |
+--------------+--------------+

For session_id 1, 2 and 3 have a duration greater or equal than 0 minutes and less than 5 minutes.
For session_id 4 has a duration greater or equal than 5 minutes and less than 10 minutes.
There are no session with a duration greater or equial than 10 minutes and less than 15 minutes.
For session_id 5 has a duration greater or equal than 15 minutes.



select '[0-5>' BIN, sum(if(duration<300,1,0)) TOTAL from Sessions 
union 
select '[5-10>' bin, sum(if(300<=duration and duration<600,1,0)) total from Sessions
union 
select '[10-15>' bin, sum(if(600<=duration and duration<900,1,0)) total from Sessions 
union 
select '15 or more' bin, sum(if(900<=duration,1,0)) total from Sessions 


SELECT '[0-5>' bin, COUNT(*) total
FROM Sessions
WHERE duration BETWEEN 0 AND 5*60
UNION ALL
SELECT '[5-10>' bin, COUNT(*) total
FROM Sessions
WHERE duration BETWEEN 5*60 AND 10*60
UNION ALL
SELECT '[10-15>' bin, COUNT(*) total
FROM Sessions
WHERE duration BETWEEN 10*60 AND 15*60
UNION ALL
SELECT '15 or more' bin, COUNT(*) total
FROM Sessions
WHERE duration >= 15*60