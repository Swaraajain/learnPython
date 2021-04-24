# #Question F1: Write a function that takes one integer argument and returns its square.
# #QuestionF2: Write a function to calculate the cube of a number.
# #Question F3: Write a function that returns 1 if the number is prime and 0 if not prime. Number is passed to the function as argument.
# #Question F4: Write a function that has two integer arguments and returns first number raised to the power second number.
# #Question F5:  Write a function to return the length of the string. String is passed to the function as argument.
#
# import math
#
# def square(x):
#     x=x*x
#     return x
#
# print(square(4))
#
# def cube(x):
#     x=x*x*x
#     return x
#
# print(cube(4))
#
# def prime(x):
#    for values in range(2,10):
#     if int(x%values)==0:
#         print ('1')
#
#     else:
#         print('0')
#
# print(prime(4))
#
# #Question F4: Write a function that has two integer arguments and returns first number raised to the power second number.
#
# def power(a,b):
#     p=a**b
#     return p
#
# print(power(2,5))
#
# #Question F5:  Write a function to return the length of the string. String is passed to the function as argument.
#
# def length(x):
#     y=len(x)
#     return y
#
# print(length("swara"))
#
# # Question B16: WAP to convert a small letter into capital letter and vice versa.

# Question B18: WAP to input the sales made by a salesman and calculate the commission according to the following conditions:
# 	 	Sales						Commission
# 1-10000					4%
# 10001-20000					5%
# 20001-30000					6%
# >30000					7%

name="sWarA"

print(name.swapcase())

newname = []
line = [x for x in name]
for value in line:
    if value.islower():
        value.upper()
        newname.append(value)
    elif value.isupper():
        value.lower()
        newname.append(value)

print("".join(newname))




# # Question B17: WAP to input the marks of a student in five subjects and calculate the grade according the following conditions:
# # 		Marks						Grade
# # 		>90						S
# 		76-90						A
# 		61-75						B
# 		51-60						C
# 		40-50						D
# 		<40						Fail

mark=[]
total = 0
for x in range(5):

    marks=int(input("enter the marks:"))
    total=total+marks
print("total",total)

percent=(total/5)
print(percent)
# if (ercent>90):
#     print("s")
# elif (90>percent>75):
#     print(A)
# elif (percent>90):
#     print("s")
#
# total=