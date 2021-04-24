# we are learning for loop

name = ['sahil','itee','swara','mikhil']
print(name[1:3])



#jiju name
print(name[3])
# itee and mikhil
namess = name[1::2]
print(namess)


arr = [1,2,3,4,5,6,7,8,9,10,11]
print(arr[::-3])

# interview question

name = "Sahil Nagpal"
print(name[::-1])



# for loop
arr = [1,2,3,4,5,6,7,8,9,10,11]

# find the even numbers
for numbers in arr:
    if numbers%2==0:
        print(numbers)

# find the odd numbers
        for numbers in arr:
            if numbers % 2 == 1:
                print(numbers)

# find the sum of all the numbers in array




# find the sum of all the even numbers in array

sum=0
for x in arr:
    if x%2==0:
        print(x)
        sum= sum+x
print(sum)

# find the count of all odd numbers and even number in an array
arr = [1,2,3,4,5,6,7,8,9,10,11,12]
count=0
for x in arr:
    if x%2==1:#odd
        count= count+1
print(f"The count of odd number is {count}")
count=0
for x in arr:
    if x%2==1:
        count= count+1

print(f"The count of even number is {count}")
print("The count of even numbers is ", count)

# find the average of array
arr = [1,2,3,4,5,6,7,8,9,10,11,12]

totalnum=0
sum=0
for x in arr:
    sum = sum+ x
    totalnum = totalnum+ 1

avg=sum/totalnum
print("the average is ",avg)
