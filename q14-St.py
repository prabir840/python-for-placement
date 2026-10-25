# 14. **Count the number of characters in a string** without using `len()`.
cyan = "\033[1;36m"
cyanClose = "\033[0m"


Str = "Hello world !"
length = 0

for i in Str:
  length = length + 1
  
print(cyan,"The length of string is -->",length, cyanClose)