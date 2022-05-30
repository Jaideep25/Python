# Taking the number 123 as n to check palindrome
n = 123

# Making a copy of the input number
temp = n

# Declaring a variable to store the reverse of the input number.
reverse = 0

# Reversing the number using while loop
while(n>0):
    digit = n % 10
    reverse = reverse*10 + digit
    n = n // 10

# Checking whether the reversed number is equal to the original number.
if(temp == reverse):
    print("Palindrome")
else:
    print("Not a Palindrome")
