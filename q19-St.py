# 19. **Find the first non-repeating character** in a string.

str = "Hello world!"

for i in str:
  if str.count(i)==1:
    print(i)
    break
else:
  print("No non-repeating character present in a string")