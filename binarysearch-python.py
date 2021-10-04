def binarySsearch(arr:list, low:int, high:int, x:int):

    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 

        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:

        return -1

n:int = int(input("Enter the max index")) 
arr:list = []
for i in range(n):
    arr.append(input(f"Element {i}: "))

x:int = int(input("Enter the digit for search: "))

result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")