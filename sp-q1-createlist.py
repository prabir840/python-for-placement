# creating list by user input

n = int(input("Enter how many number want to insert into LIST -->\n"))
arr = []
for i in range (n):
  if (i==0):
    numbers = int(input("Enter Number\n"))
  else:
    numbers = int(input("Enter Number Again \n"))
  arr.append(numbers)
print("your list is--> \n", arr)