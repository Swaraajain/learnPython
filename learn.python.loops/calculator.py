import math

def cal(num1,input,num2):
    if input=='+':
        add=num1+num2
        return add
    elif input=='-':
        sub = num1 - num2
        return sub
    elif input=='*':
        mul = num1 * num2
        return mul
    elif input=='/':
        div = num1 / num2
        return div
    elif input=='%':
        mod = num1% num2
        return mod

def scienctific_cal(input,num1):
    if input == 'cos':
        cos = math.cos(num1)
        return cos
    elif input == 'sin':
        sin = math.sin(num1)
        return sin
    elif input == 'tan':
        tan = math.tan(num 1)
        return tan

print(cal(45,'+',55))
