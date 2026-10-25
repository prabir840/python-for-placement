# 15. **Reverse a string** using a loop.

cyan = "\033[1;36m"
cyanClose = "\033[0m"

str = "Hello ji !"
n = len(str)

# print (str[1])

for i in range (n):
  print(str[n-i-1],end="")
  