# Challenge Summary
Write a function called FizzBuzzTree which takes a k-ary tree as an argument
Create a new tree with the same structure as the original, but the values modified as follows:
If the value is divisible by 3, replace the value with “Fizz”
If the value is divisible by 5, replace the value with “Buzz”
If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
If the value is not divisible by 3 or 5, simply turn the number into a String.

## Whiteboard Process
![image](../../white-bord/18.jpg?raw=true)

## Approach & Efficiency
**Big o :**
Time : O(n)
Space : O(1)

## Solution
save old k-Tree in new tree
Travel in the tree by  breadth first traversal way
check every node value and change it based on previous rolls
