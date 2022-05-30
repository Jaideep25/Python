students_arrival_time = [9,25,39,45,9,75,84,2,18,13]
 
for student_counter in range(len(students_arrival_time)):
 
    if students_arrival_time[student_counter] == 9 :
        print("On time")
        
    elif students_arrival_time[student_counter] > 9 and students_arrival_time[student_counter] <= 19:
        print("10 minutes late")
       
    elif students_arrival_time[student_counter] > 19 and students_arrival_time[student_counter] <= 39:
        print("30 minutes late")
        
    else:
        print("Zero marks")
