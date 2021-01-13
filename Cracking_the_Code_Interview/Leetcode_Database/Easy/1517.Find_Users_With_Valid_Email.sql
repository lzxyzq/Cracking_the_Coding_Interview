Table: Users

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
| mail          | varchar |
+---------------+---------+
user_id is the primary key for this table.
This table contains information of the users signed up in a website. Some e-mails are invalid.
 

Write an SQL query to find the users who have valid emails.

A valid e-mail has a prefix name and a domain where: 

The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.' and/or dash '-'. The prefix name must start with a letter.
The domain is '@leetcode.com'.
Return the result table in any order.

The query result format is in the following example.

 

Users
+---------+-----------+-------------------------+
| user_id | name      | mail                    |
+---------+-----------+-------------------------+
| 1       | Winston   | winston@leetcode.com    |
| 2       | Jonathan  | jonathanisgreat         |
| 3       | Annabelle | bella-@leetcode.com     |
| 4       | Sally     | sally.come@leetcode.com |
| 5       | Marwan    | quarz#2020@leetcode.com |
| 6       | David     | david69@gmail.com       |
| 7       | Shapiro   | .shapo@leetcode.com     |
+---------+-----------+-------------------------+

Result table:
+---------+-----------+-------------------------+
| user_id | name      | mail                    |
+---------+-----------+-------------------------+
| 1       | Winston   | winston@leetcode.com    |
| 3       | Annabelle | bella-@leetcode.com     |
| 4       | Sally     | sally.come@leetcode.com |
+---------+-----------+-------------------------+
The mail of user 2 doesnt have a domain.
The mail of user 5 has # sign which is not allowed.
The mail of user 6 doesnt have leetcode domain.
The mail of user 7 starts with a period.




select 
    user_id,
    name,
    mail
from Users where mail regexp '^[a-zA-Z]+[\\w/\\.\\-]*(@leetcode.com)$'


"双反斜杠+w"表示字母、数字、下划线，相对"a-zA-Z0-9"的写法更简洁。

^                         匹配字符串的开始部分

$                         匹配字符串的结束部分

.                          匹配任何字符（包括回车和新行）

a*                       匹配0或多个a字符的任何序列

a+                       匹配1个或多个a字符的任何序列

a?                       匹配0个或1个a字符

de|abc                匹配序列de或abc

(abc)*                匹配序列adc的0个或者多个实例

a*                    可被写为a{0,}

a+                    可被写为a{1,}

a?                    可被写为a{0,1}

匹配特殊字符

\\  为前导。即转义.正则表达式内具有特殊意义的所有字符都必须以这种方式转义。

\\-  表示查找 -

\\.  表示查找 .