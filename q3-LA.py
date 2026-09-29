# 3. Find the smallest element in a list** without using `min()`.


def FindSmallest(arr):
  smlt = arr[0]
  for i in range (len(arr)):
    if (arr[i]<smlt) :
      smlt = arr[i]
  return smlt
    
arr = [98,34,6,-4,74,3,6,9,478,5,5,3,-22]
print("\033[1;32mThe Smallest number is \033[0m",FindSmallest(arr))