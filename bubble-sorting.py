def bubbleSort(arr:int, n) -> int:
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
l:int = int(input("Enter the amx index"))
arr:list = []
for i in range(l):
    arr.append(int(input(f"{i} element: ")))            
bubbleSort(arr, len(arr))
 
print(f"Sorted array is: {', '.join([str(arr[i]) for i in range(len(arr))])}")
