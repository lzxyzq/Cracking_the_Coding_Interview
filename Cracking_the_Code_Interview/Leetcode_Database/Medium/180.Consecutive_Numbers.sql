Write a SQL query to find all numbers that appear at least three times consecutively.

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+
For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.

+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+


select 
    distinct L1.Num as ConsecutiveNums
from Logs L1 join Logs L2 
on L1.Num = L2.Num and L2.Id - L1.Id between 0 and 2
group by L1.Id,L1.Num
having count(*) = 3