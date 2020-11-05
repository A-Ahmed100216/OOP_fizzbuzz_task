# Create a class called FizzBuzz
class FizzBuzz:

    def __init__(self):
        # Create a number attribute
        self.number=[i for i in range(1,101)]

    # Create a function
    def fizzbuzz(self):
        # For each value in the number attribute range...
        for n in range(len(self.number)):
            # If the number is divisible by 5 and 3, prints FizzBuzz
            if n%3==0 and n%5==0:
                print("FizzBuzz")
            # If the number is divisible by 3, prints Fizz
            elif n%3==0:
                print("Fizz")
            # If the number is divisible by 5, prints Buzz
            elif n%5==0:
                print("Buzz")
            # Otherwise, it just prints the number
            else:
                print(n)

# Create an instance to test.
test= FizzBuzz()
print(test.fizzbuzz())
