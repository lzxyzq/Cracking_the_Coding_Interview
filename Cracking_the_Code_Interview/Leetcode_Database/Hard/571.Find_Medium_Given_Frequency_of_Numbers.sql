The Numbers table keeps the value of number and its frequency.

+----------+-------------+
|  Number  |  Frequency  |
+----------+-------------|
|  0       |  7          |
|  1       |  1          |
|  2       |  3          |
|  3       |  1          |
+----------+-------------+
In this table, the numbers are 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3, so the median is (0 + 0) / 2 = 0.

+--------+
| median |
+--------|
| 0.0000 |
+--------+
Write a query to find the median of all numbers and name the result as median.




select avg(number) median
from
    (select number,
        sum(frequency) over(order by number) asc_accumu,
        sum(frequency) over(order by number desc) desc_accumu
        from numbers) t1, 
    (select sum(frequency) total from numbers) t2
where asc_accumu >= total/2 and desc_accumu >=total/2