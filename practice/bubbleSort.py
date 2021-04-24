arr = [15,4,25,43,2]

for x in range(len(arr)):
    for y in range(len(arr)-x-1):
        if arr[y]>arr[y+1]:
            arr[y], arr[y+1] =arr[y+1], arr[y]

print(arr)