# 7. **Find the second smallest distinct number** in a list.

arr = [3,8,9,5,2,67,23,2,22,98,7,7,90]

for i in range (len(arr)-1):
  for j in range (len(arr)-1-i):
    if(arr[j]>arr[j+1]):
      arr[j],arr[j+1] = arr[j+1], arr[j]
# print(arr)

if arr[0]==arr[1]:
  print(arr[2])
else:
  print(arr[1])