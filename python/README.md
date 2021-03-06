# Data Structures and Algorithms

### 401 Data Structures, Code Challenges

## Code Challenge: Class 12

## Whiteboard Process
![image](white-bord/12.jpg?raw=true)

## Approach & Efficiency
I used class like Queue with principle first in first out
the Big O :
Time : O(n)
Space : O(2n)

## Solution
check the animal type before do any process , if the animal is cat or dog add the animal in the last of the queue
in dequeue start search from front of queue , then return the first wonted animal from front to rare

## Code Challenge: Class 08
### white-bord
![image](white-bord/8.jpg?raw=true)

## Code Challenge: Class 07
### white-bord
![image](white-bord/7.jpg?raw=true)

# Reverse an Array
we need a function , array function , for loop , list

## Challenge
Write a function called reverseArray which takes an array as an argument. Without utilizing any of the built-in methods available to your language, return an array with elements in reversed order.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## Solution
`
def reverseArray (arr):
    arr2 = []
    length = len(arr)
    for i in arr:
        arr2.append(arr[length-1])
        length -=1
    return arr2
`
# BinarySearch
# Challenge Summary
Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the search key, or -1 if the element does not exist.

## Approach & Efficiency
I used for loop to solve challenge

## Solution
using for loop array I search for key fro index zero to last item
if for statement find the key into the array the function return this key
if for statement didn't find key the function return -1

# frame
![image](white-bord/3.PNG?raw=true)


| Code Challenges                        | Status                |  Pull Request        |
| ---------------------------------------| --------------------- |--------------------- |
| Code Challenge: Class 01               |                       |        [Link]()      |
| Code Challenge: Class 02               |                       |        [Link]()      |
| Code Challenge: Class 03               |                       |        [Link]()      |
| Code Challenge: Class 04               |                       |        [Link]()      |
| Code Challenge: Class 05               |                       |        [Link]()      |

## Language: `Python`

### Folder and Challenge Setup

Each type of code challenge has slightly different instructions. Please refer to the notes and examples below for instructions for each DS&A assignment type.

### Data Structure: New Implementation

- Create a new folder under the `python` level, with the name of the data structure and complete your implementation there
  - i.e. `linked_list`
- Implementation (the data structure "class")
  - The implementation of the data structure should match package name
    - i.e. `linked_list/linked_list.py`
  - Follow Python [naming conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

    ```python
    class LinkedList:
      def __init__(self):
        # ... initialization code

      def method_name(self):
        # method body
    ```

- Tests
  - Within folder `tests` create a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Your tests will then need to require the data structure you're testing
      - i.e. `from linked_list.linked_list import LinkedList`

### Data Structure: Extending an implementation

- Work within the existing data structure implementation
- Create a new method within the class that solves the code challenge
  - Remember, you'll have access to `self` within your class methods
- Tests
  - You will have folder named `tests` and within it, a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Add to the tests written for this data structure to cover your new method(s)

### Code Challenge / Algorithm

Code challenges should be completed within a folder named `code_challenges` under the `python` level

- Daily Setup:
  - Create a new folder under the `python` level, with the name of the code challenge
    - Each code challenge assignment identifies the branch name to use, for example 'find-maximum-value'
    - For clarity, create your folder with the same name, ensuring that it's `snake_cased`
    - i.e. For a challenge named 'find_maximum_value', create the folder:`code_challenges/find_maximum_value`
  - Code Challenge Implementation
    - Each code challenge requires a function be written, for example "find maximum value"
    - Name the actual challenge file with the name of the challenge, in `snake_case`
      - i.e. `find_maximum_value.py`
    - Reminder: Your challenge file will then need to require the data structure you're using to implement
      - i.e. `from linked_list.linked_list import LinkedList`
    - Your challenge function name is up to you, but name something sensible that communicates the function's purpose. Obvious is better than clever
      - i.e. `find_maximum_value(linked_list)`
  - Tests
    - Ensure there is a `tests` folder at the root of project.
      - i.e. a sibling of this document.
    - within it, a test file called `test_[challenge].py`
      - i.e. `tests/find_maximum_value.py`
      - Your test file would require the challenge file found in the directory above, which has your exported function
        - i.e. `from code_challenges.find_maximum_value import find_maximum_value`

## Running Tests

If you setup your folders according to the above guidelines, running tests becomes a matter of deciding which tests you want to execute.  Jest does a good job at finding the test files that match what you specify in the test command

From the root of the `data-structures-and-algorithms/python` folder, execute the following commands:

- **Run every possible test** - `pytest`
- **Run filtered tests** - `pytest -k some_filter_text`
- **Run in watch mode** - `ptw` or `pytest-watch`
