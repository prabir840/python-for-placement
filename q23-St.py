# 23. **Count how many digits** are present in a string.

str = "abcd1239994"
DigitInString = 0
Digits = "1234567890"

for i in str:
  if (i in Digits):
    DigitInString +=1

print(DigitInString)