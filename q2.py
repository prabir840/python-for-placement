# Find the second Largest and Second smallest number
def FindNumber(arr):
  n = len(arr)
  for i in range (n-1):
    for j in range (n-1-i):
      if (arr[j]>arr[j+1]):
        arr[j], arr[j+1] = arr[j+1], arr[j]
  print ("Second smallest number is",arr[1],"\nSecond largest number is",arr[n-2])
  
arr = [2,6,3,1,9,5,0,86,45]

FindNumber(arr)