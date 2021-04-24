#question - find the longest word and print the word and length of the z
# question - remove the nth index element from the string
name = "My Name is Sahil Nagpal and I love Programming"
arr = name.split(" ")
counter=0
word=""
for y in arr:
    if len(y)>counter:
        counter=len(y)
        word=y
print("the length and the longest word is: ",word,counter)

print("Array",arr)
updatedString=arr.pop(int(input("enter the index number to be removed :")))
print("new string is :",arr)