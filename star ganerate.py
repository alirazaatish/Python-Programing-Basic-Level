
# for i in range(6,1,-1):
#      for j in range(1,i):
#           print("*", end='')

#      # print("\n")
#           i
# *         1
# **        2
# ***       3
# ****      4
# *****     5


# for i in range(1,6):
#      print("*"*i)

# i=1
# while i <=5:
#     print("*"*i)
#     i+=1


#        i
# *****  5 
# ****   4
# ***    3
# **     2
# *      1

# for i in range(1,6,1):
#     print("*"*(6-i))

# print(" ")

# i=1
# while i<=5:
#       print("*"*(6-i))
#       i=i+1


# pyramid pattern
# n = 5  # Change this value to adjust the size of the pyramid

# for i in range(1, n + 1):
#     spaces = ' ' * (n - i)
#     stars = '*' * (2 * i - 1)
#     print(spaces + stars)


# *********
#  *******
#   *****
#    ***
#     *

# n=5
# for i in range(1,n+1):
#     spaces="+"*i
#     stars="*"*(2*n-1)
#     print(spaces+stars)




# *********
#  *******
#   *****
#    ***
#     *
    
n=5
for i in range(n,0,-1):
    spaces=" "*(6-i)
    stars="*"*(2*i-1)
    print(spaces+stars)


