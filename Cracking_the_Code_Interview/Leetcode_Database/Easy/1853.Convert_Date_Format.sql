Table: Days

+-------------+------+
| Column Name | Type |
+-------------+------+
| day         | date |
+-------------+------+
day is the primary key for this table.
 

Write an SQL query to convert each date in Days into a string formatted as "day_name, month_name day, year".

Return the result table in any order.

The query result format is in the following example:

 

Days table:
+------------+
| day        |
+------------+
| 2022-04-12 |
| 2021-08-09 |
| 2020-06-26 |
+------------+

Result table:
+-------------------------+
| day                     |
+-------------------------+
| Tuesday, April 12, 2022 |
| Monday, August 9, 2021  |
| Friday, June 26, 2020   |
+-------------------------+
Please note that the output is case-sensitive.


/*
    %W	星期名
    %w	周的天 （0=星期日, 6=星期六）
    %M	月名
    %m	月，数值(00-12)
    %d	月的天，数值(00-31)
    %e	月的天，数值(0-31)
    %Y	年，4 位
    %y	年，2 位
*/


SELECT date_format(day, '%W, %M %e, %Y') AS day FROM days