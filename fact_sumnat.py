import math

sw = int(input("Press anyone of the following ~ \n 1. Factorial of a number \n 2. Sum of n Natural numbers\n"))

if sw == 1:
    n = int(input("Enter a number ~ "))
    print("Factorial of ",n,"is",math.factorial(n))

elif sw == 2:
    a = int(input("Enter a positive number ~ "))
    print("Sum of the natural numbers till",a,"is",(a*(a+1))/2)

else :
    print("Not for Einstein's species")
