Table: Transactions

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| transaction_id | int      |
| day            | datetime |
| amount         | int      |
+----------------+----------+
transaction_id is the primary key for this table.
Each row contains information about one transaction.
 

Write an SQL query to report the IDs of the transactions with the maximum amount on their respective day. If in one day there are multiple such transactions, return all of them.

Return the result table in ascending order by transaction_id.

The query result format is in the following example:

 

Transactions table:
+----------------+--------------------+--------+
| transaction_id | day                | amount |
+----------------+--------------------+--------+
| 8              | 2021-4-3 15:57:28  | 57     |
| 9              | 2021-4-28 08:47:25 | 21     |
| 1              | 2021-4-29 13:28:30 | 58     |
| 5              | 2021-4-28 16:39:59 | 40     |
| 6              | 2021-4-29 23:39:28 | 58     |
+----------------+--------------------+--------+

Result table:
+----------------+
| transaction_id |
+----------------+
| 1              |
| 5              |
| 6              |
| 8              |
+----------------+
"2021-4-3"  --> We have one transaction with ID 8, so we add 8 to the result table.
"2021-4-28" --> We have two transactions with IDs 5 and 9. The transaction with ID 5 has an amount of 40, while the transaction with ID 9 has an amount of 21. We only include the transaction with ID 5 as it has the maximum amount this day.
"2021-4-29" --> We have two transactions with IDs 1 and 6. Both transactions have the same amount of 58, so we include both in the result table.
We order the result table by transaction_id after collecting these IDs.
 

Follow up: Could you solve it without using the MAX() function?



SELECT
    transaction_id
FROM transactions
WHERE (left(day,10), amount) in (
    SELECT left(day,10), MAX(amount)
    FROM transactions GROUP BY DATE(day)
)
ORDER BY 1;


SELECT
    transaction_id
FROM transactions
WHERE (DATE(day), amount) in (
    SELECT DATE(day), MAX(amount)
    FROM transactions GROUP BY DATE(day)
)
ORDER BY 1;

row_number()over()：不并列连续  
rank()over()：并列，不连续  Parallel, discontinuous
dense_rank()over()：并列，连续

rank() over (partition by A order by B) 1,1,1,4
dense_rank() over (partition by A order by B) 1,1,1,2
row_number() over (partition by A order by B) 1,2,3,4
所以，此处选择rank或者dense_rank都可以


select transaction_id
from(
        select transaction_id,
        rank()over(partition by substring(day,1,10) order by amount desc) r 
        from transactions
    ) a
where a.r=1
order by 1


