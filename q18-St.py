red = "\033[1;31m"
green = "\033[1;32m"
close = "\033[0m"

# 18. **Remove all spaces** from a string.

str = "Hello boos how are you?"
# str = input("Enter a sentence..\t")
RemoveSpace = ""

for i in str:
  if (i == " "):
    RemoveSpace = RemoveSpace
  else :
    RemoveSpace += i
print("The original sentence is --> \n ", str, "\nRemove space string is -->\n",green,RemoveSpace, close)