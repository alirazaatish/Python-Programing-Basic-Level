def add(m1,m2,m3):
    total=m1+m2+m3
    per=total/3
    print(per)
    if per>=50:
       print("Pass")
    else:
       print("Fail")
    return
p=int(input("Enter the physics marks: "))
m=int(input("Enter the math marks:" ))
c=int(input("Enter the computer marks: "))
add(p,m,c)
