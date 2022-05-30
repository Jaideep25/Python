students_arrival_time = [9,25,39,45,9,75,84,2,18,13]
 
student_counter = 0
 
while student_counter < len(students_arrival_time):
 
    if students_arrival_time[student_counter] == 9 :
        print("On time")
        student_counter+=1
 
    elif students_arrival_time[student_counter] > 9 and students_arrival_time[student_counter] <= 19:
        print("10 minutes late")
        student_counter+=1
 
    elif students_arrival_time[student_counter] > 19 and students_arrival_time[student_counter] <= 39:
        print("30 minutes late")
        student_counter+=1
 
    else:
        print("Zero marks")
