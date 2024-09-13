import numpy as np

def divideTwoSets(setA, setB):
    if len(setA) != len(setB):
        return "Both sets must have the same number of elements"
    
    result = []
    for i in range(len(setA)):
        result.append(setA[i] / setB[i])
    return result

setA = [100, 50, 25]
setB = [2, 5, 1]
print(divideTwoSets(setA, setB))