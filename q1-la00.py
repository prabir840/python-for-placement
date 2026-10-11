# 1. **Find the sum of all numbers in a list** without using `sum()`.

list1 = [98,34,6,74,3,6,9,478,5,5]

length = len(list1)
sumation = 0

for i in range (length):
  sumation = sumation + list1[i]
  
print(sumation)