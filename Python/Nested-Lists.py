Name_grade= []
min_grade_1=101
min_grade_2=101
n=int(input())
for i in range (n):                              
    student = [] 
    student.append(input())
    student.append(float(input()))
    Name_grade.append(student) 
for i in range(len(Name_grade)):
    if Name_grade[i][1]<min_grade_1:
        min_grade_1=Name_grade[i][1]
for i in range(len(Name_grade)):
    if Name_grade[i][1]<=min_grade_2 and Name_grade[i][1]!=min_grade_1:
        min_grade_2=Name_grade[i][1]
min_mark_2=[]
for i in range(len(Name_grade)):
    if Name_grade[i][1]==min_grade_2:
        min_mark_2.append(Name_grade[i][0])
min_mark_2.sort()
for i in range(len(min_mark_2)):
    print(min_mark_2[i])