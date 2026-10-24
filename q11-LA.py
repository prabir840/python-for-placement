# 11. **Implement Bubble Sort** in ascending order without using `sort()` or `sorted()`.

def Bubblesort (arr):
    for i in  range (len(arr)-1):
        for j in range (len(arr)-i-1):
            if( arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)

arr = [10, 25, 40, 55, 70,1,2]
Bubblesort(arr)