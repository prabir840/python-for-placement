# 5. **Count how many even and odd numbers** are present in a list.

arr = [3, 8, 9, 5, 2, 67, 23, 2, 22, 98, 7, 90,7]
oddCount=0
evenCount=0

for i in range (len(arr)):
  if (arr[i]%2==0):
    evenCount=evenCount+1
  else:
    oddCount=oddCount+1
print("Odd count is ", oddCount, "\neven count is ", evenCount)