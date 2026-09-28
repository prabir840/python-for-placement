# count number of swap & comparisons in bubble sort

def bubblesort(arr):
  n = len(arr)
  SwapCount = 0
  ComparisionCount = 0
  for i in range (n-1):
    for j in range (n-i-1):
      if(arr[j]<arr[j+1]):
        arr[j], arr[j+1] =arr[j+1], arr[j]
        SwapCount = SwapCount + 1
    ComparisionCount = ComparisionCount + 1
  print(" Number Of swap count ",SwapCount, "\n" , "Number of Comparison count ", ComparisionCount)


arr = [2,6,3,1,9,5,0,86,45]
(bubblesort(arr))