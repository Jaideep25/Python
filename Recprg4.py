from time import *


#                   Theme ~ Synthax


sw = int(input("Enter\n 1. Display the floyd's triangle. \n 2. Display the following pattern \n\t\tA \n\t\tA  B\n\t\tA  B  C\n\t\tA  B  C  D\n\t\tA  B  C  D  E\n"))

if sw==1:
    rn = int(input("Enter the size of the triangle ~ "))
    sleep(2)
    print("The no. of rows entered are {rn} \n\t\tProcessing... \n\t\t The output ~ ")
    sleep(2)

    k = 1
    for i in range(1, rn + 1):
        for j in range(1, i + 1):
            print(k, end=" ")
            sleep(0.2)
            k += 1
        print()

elif sw==2:
    n = int(input("Enter number of rows: "))
    sleep(2)
    print("The no. of rows entered are {rn} \n\t\tProcessing... \n\t\t The output ~ ")
    sleep(2)

    for i in range(1,n+1):
        v = 65
        for j in range(1, i+1):
            print(chr(v), end=" ")
            v += 1
            sleep(0.2)
        print()