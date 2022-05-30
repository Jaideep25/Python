# My Calculator
a = int( input() )
b = int(input())
print ('enter operation: +, -, *, /')
opt = input()
 
if opt == '+':
    print (a+b)
elif opt == '-':
    print (a-b)
elif opt == '*':
    print (a*b)
elif opt == '/':
    print (a/b)
else:
    print ('invalid input')