import time
import random

numberOfComparations = 0

def quickSort(vector: list[int], firstIndex: int, finalIndex: int) -> None:
  global numberOfComparations
  startIndex = firstIndex
  endIndex = finalIndex
  pivot = vector[(firstIndex + finalIndex) // 2]

  while startIndex <= endIndex:
    while vector[startIndex] < pivot: startIndex += 1
    while vector[endIndex] > pivot: endIndex -= 1
    numberOfComparations += 1
    if startIndex <= endIndex:
      aux = vector[startIndex]
      vector[startIndex] = vector[endIndex]
      vector[endIndex] = aux
      startIndex += 1
      endIndex -= 1

  if firstIndex < endIndex: quickSort(vector, firstIndex, endIndex)
  if finalIndex > startIndex: quickSort(vector, startIndex, finalIndex)

def run(vector: list[int]) -> tuple[list[int], float]:
  vectorCopy = vector[:]
  initialTime = time.time()
  quickSort(vectorCopy, 0, len(vectorCopy) - 1)
  finalTime = time.time()
  runTime = finalTime - initialTime

  return vectorCopy, runTime

'''
vector = [1, 4, 8, 3, 6, 5, 2, 7]
quickSort(vector, 0, len(vector) - 1)
for i in vector:
  print(i)
print(numberOfComparations)
'''
