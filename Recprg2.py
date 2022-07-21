import math

sw = int(input("Enter \n 1. Area of circle. \n 2. Perimeter of circle. \n 3. Area of rectangle\n Your choice ~ "))

if sw == 1:
    rad = int(input("Enter the radius ~ "))
    print("Area of the circle is ~ ",(math.pi*rad*rad)," cm\u00B2")
elif sw == 2:
    rad = int(input("Enter the radius ~ "))
    print("Area of the circle is ~ ",(math.pi*2*rad)," cm")
elif sw == 3:
    ln = int(input("Enter the length of the rectangle ~ "))
    bd = int(input("Enter the breadth of the rectangle ~ "))
    print("Area of the rectangle ~ ",(ln*bd)," cm")

#Theme ~ Synthax