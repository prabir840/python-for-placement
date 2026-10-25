red = "\033[1;31m"
green = "\033[1;32m"
close = "\033[0m"


# 17. **Count vowels and consonants** in a string.

# str = "Hello boos how are you?"

vowels = "aeiouAEIOU"
VowelsCount = 0
ConsonanatsCount = 0


for i in str:
  if i.isalpha():
    if i in vowels:
      VowelsCount += 1
    else :
      ConsonanatsCount += 1

print ("In this string -->", str, green,"\nVowels count is -->",VowelsCount, "\nConsonants Count is -->",ConsonanatsCount, close )