class Student:
    def __init__(self, name, roll_number, age, grade):
        self.name = name
        self.roll_number = roll_number
        self.age = age
        self.grade = grade

class SchoolManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_number, age, grade):
        student = Student(name, roll_number, age, grade)
        self.students.append(student)
        print(f"Student {name} has been added to the system.")

    def remove_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print(f"Student with roll number {roll_number} has been removed.")
                return
        print(f"Student with roll number {roll_number} not found in the system.")

    def display_students(self):
        if len(self.students) == 0:
            print("No students in the system.")
        else:
            print("List of Students:")
            for student in self.students:
                print(f"Name: {student.name}, Roll Number: {student.roll_number}, Age: {student.age}, Grade: {student.grade}")

if __name__ == "__main__":
    school = SchoolManagementSystem()

    while True:
        print("\nSchool Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Display Students")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            roll_number = input("Enter roll number: ")
            age = input("Enter age: ")
            grade = input("Enter grade: ")
            school.add_student(name, roll_number, age, grade)
        elif choice == '2':
            roll_number = input("Enter roll number of the student to remove: ")
            school.remove_student(roll_number)
        elif choice == '3':
            school.display_students()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")
