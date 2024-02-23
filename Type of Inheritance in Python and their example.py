#Single Iheritance
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def start_engine(self):
        print(f"{self.year} {self.make} {self.model}'s engine is started.")

    def accelerate(self):
        self.speed += 10
        print(f"The {self.make} {self.model} is now moving at {self.speed} km/h.")

    def brake(self):
        if self.speed > 0:
            self.speed -= 10
            print(f"The {self.make} {self.model} is now moving at {self.speed} km/h.")
        else:
            print(f"The {self.make} {self.model} is already stationary.")

class Car(Vehicle):
    def honk(self):
        print(f"{self.year} {self.make} {self.model} honks the horn: Beep! Beep!")

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry", 2022)

# Using methods from both Vehicle and Car classes
my_car.start_engine()
my_car.accelerate()
my_car.brake()
my_car.honk()

#Multiple Inheritance
class Animal:
    
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} moves like an animal.")

    def make_sound(self):
        pass  # Abstract method

class Machine:
    def __init__(self, model):
        self.model = model

    def start(self):
        print(f"{self.model} machine is starting.")

    def stop(self):
        print(f"{self.model} machine is stopping.")

class Robot(Animal, Machine):
    def __init__(self, name, model):
        # Initialize attributes from both parent classes
        Animal.__init__(self, name)
        Machine.__init__(self, model)

    def make_sound(self):
        print(f"{self.name} makes beeping sounds.")

# Creating an instance of the Robot class
my_robot = Robot("Robo", "R-2000")

# Using methods from both Animal and Machine classes
my_robot.move()
my_robot.start()
my_robot.make_sound()
my_robot.stop()

#Multi_level Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self, subject):
        print(f"{self.name} with ID {self.student_id} is studying {subject}.")

class GraduateStudent(Student):
    def __init__(self, name, age, student_id, thesis_topic):
        super().__init__(name, age, student_id)
        self.thesis_topic = thesis_topic

    def research(self):
        print(f"{self.name} with ID {self.student_id} is researching '{self.thesis_topic}' for their graduate thesis.")

# Creating instances of the classes
person = Person("Alice", 25)
student = Student("Bob", 20, "S12345")
grad_student = GraduateStudent("Carol", 27, "GS98765", "Artificial Intelligence")

# Using methods from all three classes
person.introduce()
student.introduce()
student.study("Mathematics")
grad_student.introduce()
grad_student.study("Computer Science")
grad_student.research()

#Hierarchical Inheritance
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine is running.")

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def honk(self):
        print(f"The {self.year} {self.make} {self.model} honks its horn!")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def wheelie(self):
        print(f"The {self.year} {self.make} {self.model} pops a wheelie!")

# Create instances of the Vehicle, Car, and Motorcycle classes
my_vehicle = Vehicle("Generic", "Car", 2023)
my_car = Car("Toyota", "Camry", 2023, 4)
my_motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2023)

# Use the methods of these classes
my_vehicle.start_engine()
my_car.start_engine()
my_car.honk()
my_motorcycle.start_engine()
my_motorcycle.wheelie()

#Hybird Iheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")

class Enrollment:
    def __init__(self, student_id, courses):
        self.student_id = student_id
        self.courses = courses

    def enroll(self):
        print(f"Student ID {self.student_id} is enrolled in the following courses: {', '.join(self.courses)}")

class Employment:
    def __init__(self, employee_id, department):
        self.employee_id = employee_id
        self.department = department

    def hire(self):
        print(f"Employee ID {self.employee_id} is hired in the {self.department} department.")

class Student(Person, Enrollment):
    def __init__(self, name, age, student_id, courses):
        Person.__init__(self, name, age)
        Enrollment.__init__(self, student_id, courses)

    def study(self):
        print(f"{self.name} with Student ID {self.student_id} is studying.")

class Teacher(Person, Employment):
    def __init__(self, name, age, employee_id, department):
        Person.__init__(self, name, age)
        Employment.__init__(self, employee_id, department)

    def teach(self):
        print(f"{self.name} (Employee ID {self.employee_id}) is teaching in the {self.department} department.")

# Creating instances of the classes
student = Student("Alice Smith", 20, "S12345", ["Math", "Physics"])
teacher = Teacher("Bob Johnson", 35, "T98765", "Science")

# Using methods from the classes
student.introduce()
student.enroll()
student.study()

teacher.introduce()
teacher.hire()
teacher.teach()
