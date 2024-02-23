
def add(num1, num2):
    sum=num1+num2
    return sum
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

result=add(a,b)

print(f"The sum of function is",result)


def calculate_rectangle_area(length, width):
    area=length*width
    return area
a=int(input("Enter the length of the rectangle:"))
b=int(input("Enter the width of rectangle:"))
result= calculate_rectangle_area(a,b)
print(f"Total area of rectangle is:",result)
