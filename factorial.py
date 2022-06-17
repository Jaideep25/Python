res = 0
fact = 1
num = int(input("Enter a no. \n"))
for i in range(1, num+1):
    fact *= i
    res = res + (i/ fact)

print(res)
