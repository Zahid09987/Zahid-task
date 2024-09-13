import numpy as np

def getBagi(myList):
    result = myList[0]
    for num in myList[1:]:
        result /= num
    return result

myList = [100, 2, 5]
print(getBagi(myList))