# Create a class called Fizz
class FizzBuzz():

    def __init__(self):
        self.number= 10
        self.start=0
        self.end=10


    def fizz(self):
        for i in range(self.start,self.end):
            if i %3==0:
                return "Fizz"
            else:
                return i

#     def buzz(self):
#         if self.number%5==0:
#             return "Buzz"
#         else:
#             return self.number
#
#     def fizzbuzz(self):
#         if self.number%3==0 and self.number%5==0:
#             return "FizzBuzz"


fizzy=FizzBuzz()
print(fizzy.fizz())
# print(fizzy.buzz())
# * Write a program that prints the numbers from 1 to 100.
# * For multiples of three print "Fizz" instead of the number
# * For the multiples of five print "Buzz" instead of the number
# * For numbers which are multiples of both three and five print "FizzBuzz"