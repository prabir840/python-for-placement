# 13. **Merge two already sorted lists** into one sorted list without calling a sorting function.

list1 = [ 1,2,3,4,5,6]
list2 = [7,8,9,10,11,12]

MergeList = []

length = len(list1) + len(list2)
n = len(list1)

for i in range (len(list1)):
  if (list1[i] is not MergeList):
          MergeList.append(list1[i])
  
for j in range (len(list2)):
  if (list2[j] is not MergeList):
          MergeList.append(list2[j])

print("\033[1;32m Here is the merged list of--> \033[0m\n\033[1;36m",list1,"\n",list2,"\033[0m\n\033[1;31m  ---> \t",MergeList,"\033[0m")