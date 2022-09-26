# Write your MySQL query statement below
SELECT name
FROM Customer
WHERE ISNULL(referee_id) or referee_id != 2;