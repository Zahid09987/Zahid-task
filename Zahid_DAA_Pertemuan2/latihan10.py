import numpy as np

def subtractTwoSets(setA, setB):
    if len(setA) != len(setB):
        return "Both sets must have the same number of elements"
    
    result = []
    for i in range(len(setA)):
        result.append(setA[i] - setB[i])
    return result

setA = [100, 50, 25]
setB = [10, 5, 1]
print(subtractTwoSets(setA, setB))