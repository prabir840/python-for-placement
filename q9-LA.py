# 9. Given numbers from `1` to `n` with one number missing, **find the missing number**.

numbers = [1,2,3,4,5,7,8,9,10]

MissingNumber = 0

for i in range (len(numbers)+2):
    if i not in numbers:
        MissingNumber=i
print(MissingNumber)
