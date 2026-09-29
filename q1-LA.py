# Find the sum of all numbers in a list** without using sum()

arr = [98,34,6,74,3,6,9,478,5,5,3]

TotalSum = 0 
for i in range (len(arr)):
  TotalSum = TotalSum + arr[i]
print("Total sum of the list", arr,"\nis ",TotalSum)