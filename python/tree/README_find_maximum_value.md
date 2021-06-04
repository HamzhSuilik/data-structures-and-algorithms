# Challenge Summary
Write an function called find-maximum-value. Without utilizing any of the built-in methods available to your language, return the maximum value stored in the tree.

## Whiteboard Process
![image](https://github.com/HamzhSuilik/data-structures-and-algorithms/blob/main/python/white-bord/16.jpg?raw=true)

## Approach  &  Efficiency
**Big O :**
- Time : (n)
- space : (2n)

## Solution
- create a function to travel in the tree like preOrder method
- in every iteration check if the node have value lager than previous value and return the largest value
- finally return the largest valuee
