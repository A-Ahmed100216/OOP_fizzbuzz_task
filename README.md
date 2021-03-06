# Task 1 -Fizz Buzz!

### Summary
This is a simple game that will substitute multiples of 3 and 5 for fizz and buzz respectively, or fizzbuzz for multiples of both 5 and 3.

### Tasks

#### Core
* Write a program that prints the numbers from 1 to 100.
* For multiples of three print "Fizz" instead of the number
* For the multiples of five print "Buzz" instead of the number
* For numbers which are multiples of both three and five print "FizzBuzz".

#### Extra
* Make a new fizzbuzz file and make it functional
* Make it so we we can decide which numbers to substitute for fizz and buzz using functions


### Acceptance Criteria
* All core task are done
* Code works with no error
* Implement OOP
  * Create a parent class 
  * Create the required function, implementing DRY
* At least 3 commits.


# Process
#### 1. Class Creation
* Create a class called FizzBuzz. This is a parent class.
```python
class FizzBuzz:
```

* Initialise the class with an attributes to store the start and end numbers.
```python
    def __init__(self):
        self.start = 1
        self.end = 101
```

* Create the fizzbuzz function and use control flow to define the criterion.
  * If the number is a multiple of 3 - print "Fizz"
  * If the number is a multiple of 5 - print "Buzz"
  * If the number is a multiple of 3 and 5 - print "FizzBuzz"
  * Else, print the number. 
```python
    def fizzbuzz(self):
        for n in range(self.start, self.end):
            if n%3==0 and n%5==0:
                print("FizzBuzz")
            elif n%3==0:
                print("Fizz")
            elif n%5==0:
                print("Buzz")
            else:
                print(n)
```
#### 2. Instantiation
* Create a new file and import the FizzBuzz class.
```python
from fizz import FizzBuzz
```

* Create an instance of the class in order to test the code.
```python
test= FizzBuzz()
test.fizzbuzz()
```

#### Extra
* We can add increased functionality, allowing the user to substitute their own numbers using the following inputs:
```python
self.fizz=int(input("Please enter the number you wish the substitute with Fizz: "))
self.buzz=int(input("Please enter the number you wish the substitute with Buzz: "))
```
* Upon adding these attributes, the control flow must be changed to reflect this. 
* It is important to convert the fizz and buzz attributes into integers.
```python
    def fizzbuzz(self):
        # For each value in the number attribute range...
        for n in range(self.start, self.end):
            # If the number is divisible by int Fizz and int Buzz, prints FizzBuzz
            if n%self.fizz==0 and n%self.buzz==0:
                print("FizzBuzz")
            # If the number is divisible by int Fizz, prints Fizz
            elif n%self.fizz==0:
                print("Fizz")
            # If the number is divisible by int Buzz, prints Buzz
            elif n%self.buzz==0:
                print("Buzz")
            # Otherwise, it just prints the number
            else:
                print(n)
```

