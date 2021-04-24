from collections import Counter

arr = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,1,1,1]

print(Counter(arr))

print(dict((i,arr.count(i))for i in arr))
