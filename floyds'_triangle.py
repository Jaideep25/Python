rn = int(input("Enter the size of the triangle ~ "))
k = 1
for i in range(1, rn + 1):
    for j in range(1, i + 1):
        print(k, end=" ")
        k += 1
    print()