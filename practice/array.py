# arr = []
# length= (int(input("please enter the length :")))
# for x in range(length):
#     arr.append(int(input("please enter the elements")))
#
# print(arr)

# print a function to find maximum of three numbers
# print a function to find the count upper case and lower case elements

array=[1,23,39]
max=0


def max_num():
    global max
    for x in array:
        if x > max:
            max = x


max_num()



# def max(array):
#     max=0
#     for x in array:
#         if x > max:
#             max = x
#
#     return max
#
# print(max([1,2,3,4,5,6,7]))



def cases(string):
    upper=0
    lower=0
    for x in string:
        if (x.isupper()):
            upper=upper+1
        elif x in ('*','#',',','!'):
            print("This also have wild characters")
        else:
            lower=lower+1
    print("uppercase Characters are:",upper)
    print("lowercase Characters are:", lower)

    return ''

print(cases("SwaraJAin*"))