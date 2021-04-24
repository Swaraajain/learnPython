import math


def area_of_shape(shape):
    if shape in ('Circle','circle'):
        radius = int(input("Please enter the radius : "))
        area = math.pi * math.pow(radius,2)

    elif shape in ('rectangle','Rectangle'):
        length = int(input("PLease enter the lemgth : "))
        height = int(input("PLease enter the height : "))
        breadth = int(input("PLease enter the breadth : "))
        area = length * breadth * height

    return area


#print(area_of_shape("Circle"))


name = input("Enter the name : ")
print(name.lower())


Question A23: WAP to input employee code, name and basic salary of an employee and
calculate the following values:

HRA 40 % of basic salary
DA 10 % of basic salary
CCA 5 % of basic salary
GS Basic + HRA + DA + CCA
PF 10 % of GS
IT 10 % of GS
NS GS – (PF + IT)

