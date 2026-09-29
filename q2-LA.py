# Find the largest element in a list** without using `max()`.

def FindLargest(arr):
  lrg=0
  for i in range (len(arr)-1):
    if (arr[i]>lrg) :
      lrg = arr[i]
  print(lrg)
    
arr = [98,34,6,74,3,6,9,478,5,5,3]
FindLargest(arr)