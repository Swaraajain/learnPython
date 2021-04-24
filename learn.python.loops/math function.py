# # #Question F1: Write a function that takes one integer argument and returns its square.
# import math
# def Square(x):
#     return math.pow(x,2)
#
# print(Square(4))
#
# #QuestionF2: Write a function to calculate the cube of a number.
# def cube(x):
#     return math.pow(x, 3)
#
# print(cube(40))
#
# #Question F3: Write a function that returns 1 if the number is prime and 0 if not prime. Number is passed to the function as argument.
#
# def prime(x):
#     for y in range(2,x-1):
#         if (x%y)==0:
#            return print("its not prime")
#         else:
#             return print("a prime")
#
# print(prime(13))
#
# # Question F4: Write a function that has two integer arguments and returns first number raised to the power second number.
# def power(x,y):
#     return math.pow(x, y)
#
# print(power(2,5))
# #Question F5:  Write a function to return the length of the string. String is passed to the function as argument.
#
# def length(x):
#     return len(x)
#
# print(length("swara"))
#
# #Question B16: WAP to convert a small letter into capital letter and vice versa.
#
# def caseConvert(x):
#     return x.swapcase()
#
# print(caseConvert("swarA"))
# # Question B17: WAP to input the marks of a student in five subjects and calculate the grade according the following conditions:
# # # 		Marks						Grade
# # # 		>90						S
# # 		76-90						A
# # 		61-75						B
# # 		51-60						C
# # 		40-50						D
# # 		<40						Fail
#
# total = 0
# for x in range(5):
#
#     marks=int(input("enter the marks on 20:"))
#     total=total+marks
# print("total",total)
#
# if total>90:
#     print("S")
# elif total<=90 and total>=76:
#     print("A")
# elif total<=75 and total>=61:
#     print("B")
# elif total<=60 and total>=51:
#     print("C")
# elif total<=50 and total>=40:
#     print("D")
# else:
#     print("fail")
#
# # Question B18: WAP to input the sales made by a salesman and calculate the commission according to the following conditions:
# # 	 	Sales						Commission
# # 1-10000					4%
# # 10001-20000					5%
# # 20001-30000					6%
# # >30000					7%
#
# commission=int(input("enter the total sales amount:"))
#
# if commission>=1 and commission<=10000:
#     amount=commission*.04
#     print("Total commission is :",amount)
# if commission>=10001 and commission<=20000:
#     amount=commission*.05
#     print("Total commission is :", amount)
# if commission>=20001 and commission<=30000:
#     amount=commission*.06
#     print("Total commission is :", amount)
# if commission<=30000:
#     amount=commission*.07
#     print("Total commission is :", amount)
#

#Write a function that prints the sum of the digits, count of the digits and reverse of a number. Number is passed to the function as argument.

def sum_count_reverse(x):
    numbers = [int(value) for value in str(x)]
    print(numbers)
    sum=0
    for vals in numbers:
        sum=sum+vals
    return sum,len(numbers),  numbers[::-1]
print(sum_count_reverse(1234567))

