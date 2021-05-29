# Challenge Summary
 write function should take a string as argument, and should return a boolean representing whether or not the brackets in the string are balanced

## Whiteboard Process
![image](../white-bord/13.jpg?raw=true)

## Approach & Efficiency
I used level system to solve the problem , I give 1 for [ , 2 for ( and 3 for {
and I used level variable to ensure the order of brackets is right


## Solution
when the function discover open brackets add the static brackets value to sum variable * current level and then move to the next level
when the function discover close brackets subtract the static brackets value from sum variable * current level and then go back to the previous level
the level start from 1 and when the function discover open brackets the function move to the next level by multi level by 10
if final sum equal zero the brackets in the string are balanced else return False



