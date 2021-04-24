
# find out the positive numbers from a list

arr = [1,2,3,4,-6,9,-7,-2,-6]

for x in arr:
    if x>0:
        print(x)

# find out the sum of all positive and negative numbers from a list

arr = [1,2,3,4,-6,9,-7,-2,-6]

sum=0
for x in arr:
    if x>0:
        sum=sum+x

print("the sum of positive numbers",sum)

sum=0
for x in arr:
    if x<0:
        sum=sum+x

print("the sum of negative numbers",sum)


# find out the factorial of a number (number is taken as input)
num=int(input("enter the number to find out factorial"))
fact=1
while num >0:
    fact=fact*num
    num=num-1
print(fact)






