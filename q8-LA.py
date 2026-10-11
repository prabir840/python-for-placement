# 8. **Remove duplicates from a list** while keeping the original order.

arr = [3,8,9,5,2,67,23,23,2,22,98,7,90,2,8]
Nandita = []

for i in range (len(arr)):
  if (arr[i] not in Nandita):
    Nandita.append(arr[i])
      
print(Nandita)

# for i in range (len(arr)):
#   duplicate = False
  
#   for j in range (len(arr)-i):
#     if (arr[i]==Nandita[j]):
#       duplicate = True
      
#   if (duplicate == False):
#     Nandita.append(arr[i])
    
# print(Nandita)

