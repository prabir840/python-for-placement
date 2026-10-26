red = "\033[1;31m"
green = "\033[1;32m"
close = "\033[0m"


# 21. **Check whether two strings are anagrams** of each other.
str1 = input("Enter your First string to check Anagrams-->\t")
str2 = input("Enter your Second string to check Anagrams-->\t")

# print(sorted(str1))

if (sorted(str1) == sorted(str2)):
  print(green,"Two strings are anagrams",close)
else:
  print(red,"two strings are Not anagrams",close)