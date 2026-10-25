# 10. Perform a **linear search** and return the index of a target value; return `-1` when it is absent.

numbers = [10, 25, 40, 55, 70]

targetValue = int(input("\033[35mEnter your target value-->\t"))
ret = 0

for i in range (len(numbers)):
    if(targetValue == numbers[i]):
        ret = 1
        break
        
if(ret == 1):
    print("the index of a target value", targetValue,"is ", i)
else:
    print("-1")
