# 12. In **Bubble Sort, count the total number of comparisons and swaps** made for a given list.

def Bubblesort (arr):
    comparisons = 0
    swaps = 0

    for i in  range (len(arr)-1):
        for j in range (len(arr)-i-1):
            comparisons = comparisons+1
            if( arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swaps = swaps + 1
    print("Number of comparisons -->",comparisons,"\nNumber of swaps -->", swaps)

arr = [10, 25, 40, 55, 70,1,2]
Bubblesort(arr)