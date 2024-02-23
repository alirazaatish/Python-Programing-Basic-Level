
student_marks={
    "Ali":79,
    "Ahmad":76,
    "Raza":56,
    "Saqib":67
}

student_marks["Atish"]=99


student_grade={}
for student in student_marks:     #Ali
    marks=student_marks[student]
    if marks>=90:
        student_grade[student]="A+"if marks>=80:
        student_grade[student]="A"
    elif marks>=80:
        student_grade[student]="A"
    elif marks>=70:
        student_grade[student]="B"
    elif marks>=60:
        student_grade[student]="C"
    elif marks>=50:
        student_grade[student]="D"
print(student_grade)