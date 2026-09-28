def bubblesort(arr):
  n = len(arr)
  for i in range (n-1):
    for j in range (n-i-1):
      if(arr[j]<arr[j+1]):
        arr[j], arr[j+1] =arr[j+1], arr[j]
  return arr


arr = [2,6,3,1,9,5,0,86,45]
print(bubblesort(arr),len(arr))