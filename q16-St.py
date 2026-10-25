# 16. **Check whether a string is a palindrome.**
red = "\033[1;31m"
green = "\033[1;32m"
close = "\033[0m"


str = input("Enter a String--> \t")
n = len(str)
EmptyString = ""

for i in range (n):
  EmptyString = EmptyString + str[n-i-1]

if (str == EmptyString):
  print(str,green, " --> is a Palindrome\033[0m",close)
else: 
    print(str,red, "--> is NOT a Palindrome", close)




# a = " hello "
# b = "world"
# c = a+b 
# print (c)
