import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols=['!','@','#','$','%','^','&','*','(',')','_','+']
numbers=['0','1','2','3','4','5','6','7','8','9']

print("Wellcome to password Generator!")
n_letters=int(input("How many letters you wants in your password\n"))
n_symbols=int(input("How many symbols you want in your password\n"))
n_numbers=int(input("How many numbers you want in your password\n"))

password_list=[]

for i in range(1,n_letters):
     char=random.choice(letters)
     password_list+=char
print(password_list, end=" ")

for i in range(1,n_symbols):
     char=random.choice(symbols)
     password_list+=char
print(password_list)

for i in range(1,n_numbers):
     char=random.choice(numbers)
     password_list+=char
print(password_list)

random.shuffle(password_list)
print(password_list)	
password=" "
for i in password_list:
    password+=i 
print(password)


