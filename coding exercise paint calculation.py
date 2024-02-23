import math
def paint_calculation(height, width, coverg):
    area=height*width
    no_of_cans= math.ceil(area/coverg)
    print(f"You will need {no_of_cans} of cans to paint")

h=int(input("Enter the hight of wall in meters:\n"))
w=int(input("Enter the width of the wall in meters:\n"))
coverge=20

paint_calculation(width=w, height=h, coverg=coverge)
