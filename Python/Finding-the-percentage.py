n = int(input())
student_marks = {}
for _ in range(n):
    name, Maths,Pysics,Chemstry = input().split()
    Maths,Pysics,Chemstry=float(Maths),float(Pysics),float(Chemstry)
    scores=((Maths+Pysics+Chemstry)/3)
    student_marks[name] = scores
query_name = input()
for Name,avarage in student_marks.items():
    if Name==query_name:
        print("{:0.2f}".format(avarage))