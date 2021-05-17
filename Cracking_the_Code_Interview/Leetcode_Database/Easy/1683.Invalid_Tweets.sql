Table: Tweets

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key for this table.
This table contains all the tweets in a social media app.
 

Write an SQL query to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

Return the result table in any order.

The query result format is in the following example:

 

Tweets table:
+----------+----------------------------------+
| tweet_id | content                          |
+----------+----------------------------------+
| 1        | Vote for Biden                   |
| 2        | Let us make America great again! |
+----------+----------------------------------+

Result table:
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
Tweet 1 has length = 14. It is a valid tweet.
Tweet 2 has length = 32. It is an invalid tweet.


char_length()计算字符长度，汉字和字母都算一个字符。

1、char_length(str)
（1）计算单位：字符
（2）不管汉字还是数字或者是字母都算是一个字符
2、length(str)
（1）计算单位：字节
（2）utf8编码：一个汉字三个字节，一个数字或字母一个字节。
（3）gbk编码：一个汉字两个字节，一个数字或字母一个字节。


select
    tweet_id
from Tweets
where char_length(content) > 15