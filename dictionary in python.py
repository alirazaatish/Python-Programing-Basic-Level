#Dictionary in python
student_data={
           'Name':'Aimen',
           'Age':15,
           'grade':'A'
             }
print("Name of student is=",student_data['Name'])
print("Age of student is=", student_data['Age'])
print("Grade is=",student_data['grade'])

#Modifing new dictionary value
student_data['Name']='Ali'
student_data['Age']=17
student_data['grade']='A+'
print(student_data)

#deleting dictionary value
del student_data['grade']
print(student_data)

if 'Age' in student_data:
    print("Yes grade in student-data")
else:
    print("Grade not in student_data")

#Nested Dictionary in python

student_data={
            'Atish':{'roll_no':1,'age':17,'course':'python'},
            'Ali':{'roll':31,'age':15,'course':'java'}        
            }
print("Roll_no of Atish",student_data['Atish']['roll_no'])
print("Age of Ali",student_data['Ali']['age'])

del student_data['Atish']['course']

print(student_data['Atish'])