'''
Write a menu driven program 
a)	To input two numbers & display the larger/smaller/equal number.
b)	To read name, roll number, 5 subject marks. Calculate the average and print the report card of a student.
'''
#   Theme ~ Synthax
sw = int(input("Enter \n 1. For displaying the largest no. \n 2. To print the report card.\n"))
if sw == 1:
    n1 = int(input("Enter 2 nos. \n"))
    n2 = int(input())
    if(n1>n2):
        print("First no. is the largest.")
    elif(n1<n2):
        print("Second no. is the largest")
    else:
        print("Both the nos. are equal.")
elif sw == 2:
    avg=0
    nm = input("Enter your name ~ ")
    rn = input("Enter your roll no. ~ ")
    print("Enter 5 marks ~ \n")
    for i in range(6):
        num = int(input())
        avg += num

    print("Average ~ ",(avg/5))