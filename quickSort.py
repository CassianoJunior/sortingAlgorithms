import time
import random

numberOfComparations = 0

def quickSort(vector: list[int], firstIndex: int, finalIndex: int) -> None:
  global numberOfComparations
  startIndex = firstIndex
  endIndex = finalIndex
  pivot = vector[(firstIndex + finalIndex) // 2]

  while startIndex <= endIndex:
    while vector[startIndex] < pivot: 
      startIndex += 1
      numberOfComparations += 1
    while vector[endIndex] > pivot: 
      endIndex -= 1
      numberOfComparations += 1
    numberOfComparations += 1
    if startIndex <= endIndex:
      aux = vector[startIndex]
      vector[startIndex] = vector[endIndex]
      vector[endIndex] = aux
      startIndex += 1
      endIndex -= 1
  numberOfComparations += 1
  if firstIndex < endIndex: quickSort(vector, firstIndex, endIndex)
  numberOfComparations += 1
  if finalIndex > startIndex: quickSort(vector, startIndex, finalIndex)

def run(vector: list[int]) -> tuple[list[int], float]:
  vectorCopy = vector[:]
  initialTime = time.time()
  quickSort(vectorCopy, 0, len(vectorCopy) - 1)
  finalTime = time.time()
  runTime = finalTime - initialTime

  return vectorCopy, runTime

'''
vector = [1, 2, 3, 4, 5, 6, 7, 8]
quickSort(vector, 0, len(vector) - 1)
for i in vector:
  print(i)
print(numberOfComparations)
'''

