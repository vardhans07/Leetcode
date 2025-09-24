/*Find the names of the customer that are either: referred by any customer 
with id != 2. not referred by any customer. Return the result table in any order. 
The result format is in the following example. Example 1: 
Input: 
Customer =
| id | name | referee_id |
| -- | ---- | ---------- |
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
Output
| name |
| ---- |
| Will |
| Jane |
| Bill |
| Zack |
Expected
| name |
| ---- |
| Will |
| Jane |
| Bill |
| Zack |
*/


--# Write your MySQL query statement below


SELECT  name FROM Customer WHERE referee_id !=2 OR referee_id IS NULL;



