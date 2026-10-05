# Return length of largest word in sentence

#<------------ PART 1(using Function)------------->
sentence = "Type a Sentence"
  
SentenceArr = sentence.split()
largest = 0

for i in range (len(SentenceArr)):
  if (largest < len(SentenceArr[i])):
    largest = len(SentenceArr[i])
    
print(largest)


#<------------ PART 2(Without Function)------------->
sentence = "Type a Sentence"

SentenceArr = []
word = ""

for i in range (len(sentence)):
  if(sentence[i]!=" "):
    word = word+sentence[i]
  else:
    SentenceArr.append(word)
    word = ""
SentenceArr.append(word)


largest = 0
for i in range (len(SentenceArr)):
  if (largest < len(SentenceArr[i])):
    largest = len(SentenceArr[i])
  
print(largest)