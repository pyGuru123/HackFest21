arr = []
n = int(input("Enter number of elements in array: "))
for i in range(0, n):
    x = int(input("Enter elements: "))
    arr.append(x)
print("Unsorted array: ", arr)
l = len(arr)
for i in range(l-1):
    for j in range(0,l-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print ("Sorted array: ",arr)
