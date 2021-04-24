def sort(arr):
    for x in range(len(arr)-1):
    # To find the minimum value of the unsorted segment
    # We first assume that the first element is the lowest
    # We then use y to loop through the remaining elements
        for y in range(x+1,len(arr)):
            temp = 0
            if arr[y] < arr[x]:
            # Update the min_index if the element at x is lower than it
                temp = arr[x]
                arr[x] = arr[y]
                arr[y] = temp
    return arr
            # After finding the lowest item of the unsorted regions, swap with the first unsorted item

arr = [2,5,6,3,8,4]
print(sort(arr))

calc function
