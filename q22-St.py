# 22. **Find the longest word** in a sentence.

sentence = "hey boos how are you ?"
largestWord = 0

arr = sentence.split()

for i in range (len(arr)):
  if (largestWord<(len(arr[i]))):
    largestWord = len(arr[i])

print (largestWord)