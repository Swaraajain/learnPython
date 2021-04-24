a= int(input("provide first number : "))
b= int(input("provide second number : "))
sign= input("the operation : ")

def calc(a,b):
    if sign == '+':
        c= a+b

    elif sign== '-':
        c= a-b

    elif sign=='*':
        c= a*b

    elif sign=='/':
        c= a/b

    else:
        print("This option is not available")
    return c

print("the answer is : ",calc(a,b))


