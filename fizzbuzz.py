#Take input from the user. If the input is divisible by 3 then print "Fizz",
#if the input it divisible by 5 then print "Buzz".
#If the input is divisible by 3 and 5 then print "Fizz Buzz".

user1 = int(input("Enter number: "))
if user1 % 3 == 0 and user1 % 5 == 0:
    print("Fizz Buzz")
elif user1 % 3 == 0:
    print("Fizz")
elif user1 % 5 == 0:
    print("Buzz")
