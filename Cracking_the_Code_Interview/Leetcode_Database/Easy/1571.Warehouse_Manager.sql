Table: Warehouse

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| name         | varchar |
| product_id   | int     |
| units        | int     |
+--------------+---------+
(name, product_id) is the primary key for this table.
Each row of this table contains the information of the products in each warehouse.
 

Table: Products

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| product_name  | varchar |
| Width         | int     |
| Length        | int     |
| Height        | int     |
+---------------+---------+
product_id is the primary key for this table.
Each row of this table contains the information about the product dimensions (Width, Lenght and Height) in feets of each product.


select 
warehouse_name, 
sum(volume) as volume 
from
(select w.name as warehouse_name, 
w.product_id, w.units * Width * Length * Height as volume 
from Warehouse w 
left join Products p 
on w.product_id = p.product_id) t
group by warehouse_name