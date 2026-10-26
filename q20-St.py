# 20. **Build a character-frequency dictionary** for a string.

str = "Hello"
frequency = {}
# print(frequency)
# frequency["Hello Duniya !"]=1
# print(frequency)


for i in str :
  if i in frequency:
    frequency[i] += 1
  else:
    frequency[i] = 1
print(frequency)