# Hashmap LEFT JOIN
The SQL LEFT JOIN returns all rows from the left table, even if there are no matches in the right table. This means that if the ON clause matches 0 (zero) records in the right table; the join will still return a row in the result, but with NULL in each column from the right table.

## Challenge
Write a function that LEFT JSON two hashmaps into a single data structure

## Approach & Efficiency
Big (O):
Time -> O(n)
Space -> O(1)

## Whiteboard Process
![image](../../white-bord/33.jpg?raw=true)


## pull Request :
https://github.com/HamzhSuilik/data-structures-and-algorithms/pull/41
https://github.com/HamzhSuilik/data-structures-and-algorithms/pull/47

- [x] create left_join.py and test files
- [x] write left_join function
- [x] add tests unit to test the left_join function
- [x] prepare README file
