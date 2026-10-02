# 6. **Find the second largest distinct number** in a list.

def BubblSort(arr):
  n= len(arr)
  for i in range (n-1):
    for j in range (n-1-i):
      if (arr[j]>arr[j+1]):
        arr[j],arr[j+1]=arr[j+1],arr[j]
  return arr[n-2]

arr = [3, 8, 9, 5, 2, 67, 23, 2, 22, 98, 7, 90,7,68,69]
print(BubblSort(arr))