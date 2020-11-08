# Create a class called FizzBuzz
class FizzBuzz:

    def __init__(self):
        # Create start and end number attributes
        self.start = 1
        self.end = 101
        self.fizz=int(input("Please enter the number you wish the substitute with Fizz: "))
        self.buzz=int(input("Please enter the number you wish the substitute with Buzz: "))



    # Create a function
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


