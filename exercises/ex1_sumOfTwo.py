"""
A partir de duas listas desordenadas, desenvolva uma função que busque um par (um em cada lista), onde a soma resulte em v
"""
import random

def sumOfTwo(listA: list, listB:list, v):
    
    setB = set(listB)

    for i in range(len(listA)):
        if v-listA[i] in setB:
            return True

    return False

listA = [round(random.randint(10,10000)) for _ in range(1000000)] 
listB = [round(random.randint(10,10000)) for _ in range(1000000)] 

print(sumOfTwo(listA, listB, 5))
print(sumOfTwo(listA, listB, 50))
