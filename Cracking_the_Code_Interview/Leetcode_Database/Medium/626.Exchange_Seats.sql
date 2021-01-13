Mary is a teacher in a middle school and she has a table seat storing students names and their corresponding seat ids.

The column id is continuous increment.
 

Mary wants to change seats for the adjacent students.
 

Can you write a SQL query to output the result for Mary?
 

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
For the sample input, the output is:
 

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+


select
    (case
      # 当座位号是奇数并且不是不是最后一个座位号时
        when mod(id, 2) != 0 and counts!= id then id + 1
       # 当座位号是奇数并且是最后一个座位号时，座位号不变
        when mod(id, 2) != 0 and counts = id then id
       # 当座位号是偶数时
        else id - 1
    end) as id,student
from seat,(select count(*) as counts from seat) as b
order by id asc