# input is taken from the user
number = int(input("Please input a number "))
# Variable result is initialized
result = 0
# cube of each digit is added to find the sum
temporary = number
while temporary > 0:
	  digit = temporary % 10
	  result += digit ** 3
	  temporary //= 10
# result is displayed
if number == result:
	  print(number," - an Armstrong number")
else:
	  print(number," - not an Armstrong number")
