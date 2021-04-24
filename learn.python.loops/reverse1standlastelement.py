arr = [1,2,3,4,5,6]

# find the minimum element and the maximum element

print(max(arr))
print(min(arr))
max = 0
for x in arr:
    if x > max:
        max = x
print(max)
min = max
for x in arr:
    if x < min:
        min = x
print(min)