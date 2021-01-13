Table: Spending

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| spend_date  | date    |
| platform    | enum    | 
| amount      | int     |
+-------------+---------+
The table logs the spendings history of users that make purchases from an online shopping website which has a desktop and a mobile application.
(user_id, spend_date, platform) is the primary key of this table.
The platform column is an ENUM type of ('desktop', 'mobile').
Write an SQL query to find the total number of users and the total amount spent using mobile only, desktop only and both mobile and desktop together for each date.

The query result format is in the following example:

Spending table:
+---------+------------+----------+--------+
| user_id | spend_date | platform | amount |
+---------+------------+----------+--------+
| 1       | 2019-07-01 | mobile   | 100    |
| 1       | 2019-07-01 | desktop  | 100    |
| 2       | 2019-07-01 | mobile   | 100    |
| 2       | 2019-07-02 | mobile   | 100    |
| 3       | 2019-07-01 | desktop  | 100    |
| 3       | 2019-07-02 | desktop  | 100    |
+---------+------------+----------+--------+

Result table:
+------------+----------+--------------+-------------+
| spend_date | platform | total_amount | total_users |
+------------+----------+--------------+-------------+
| 2019-07-01 | desktop  | 100          | 1           |
| 2019-07-01 | mobile   | 100          | 1           |
| 2019-07-01 | both     | 200          | 1           |
| 2019-07-02 | desktop  | 100          | 1           |
| 2019-07-02 | mobile   | 100          | 1           |
| 2019-07-02 | both     | 0            | 0           |
+------------+----------+--------------+-------------+ 
On 2019-07-01, user 1 purchased using both desktop and mobile, user 2 purchased using mobile only and user 3 purchased using desktop only.
On 2019-07-02, user 2 purchased using mobile only, user 3 purchased using desktop only and no one purchased using both platforms.




select
    spend_date, platform,
    ifnull(sum(total_am),0) total_amount,
    ifnull(sum(total_u),0) total_users
from
(
    select p.spend_date, p.platform, t.total_am, t.total_u
    from
    (
        select distinct spend_date, "desktop" platform from Spending
        union
        select distinct spend_date, "mobile" platform from Spending
        union
        select distinct spend_date, "both" platform from Spending
    ) p
    left join
    (
        select spend_date, 
            if(count(distinct platform)=1, platform, 'both') plat,
            sum(amount) total_am,
            count(distinct user_id) total_u
        from Spending
        group by spend_date, user_id
    ) t
    on p.platform = t.plat and p.spend_date = t.spend_date
) temp
group by spend_date, platform

