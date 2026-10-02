# 4. **Reverse a list** without using `reverse()` or slicing.

arr = [3,8,9,5,2,67,23,2,22,98,7,90]
Revarr = []
n=len(arr)
for i in range (len(arr)):
  Revarr.append(arr[n-i-1])

print(Revarr)