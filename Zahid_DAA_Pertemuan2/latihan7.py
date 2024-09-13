import numpy as np

def getKali(myList):
    result = 1
    for num in myList:
        result *= num
    return result

myList = [1, 2, 3, 4]
print(getKali(myList))