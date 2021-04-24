#Write a function to search a string in the array of strings. String and array of strings should be passed to the function as parameters

name = ["sahik","Manish","Rachit","Carl"]
inputName = input("enter the string that needs to be known if present or not :")
# chek if inputName is in name or not
def Search(name,inputName):
    for x in name:
        if x.lower() in inputName.lower():
            print("The string is present")
            break
    else:
        print("The string is not present")



#         if x.__contains__(y): # magic function
#             print("the array contains this string")
#         else:
#             print("the array does not contains the string")
#
Search(name,inputName)

