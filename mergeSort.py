import time

numberOfComparations = 0

def merge(vector: list[int], initialIndex: int, middleIndex: int, finalIndex: int) -> None:
  global numberOfComparations
  leftArray = vector[initialIndex:middleIndex+1]
  rightArray = vector[middleIndex+1:finalIndex+1]

  leftArraySize = len(leftArray)
  rightArraySize = len(rightArray)

  indexLeftArray = 0
  indexRightArray = 0

  for i in range(initialIndex, finalIndex + 1):
    if indexLeftArray >= leftArraySize:
      vector[i] = rightArray[indexRightArray]
      indexRightArray += 1
    elif indexRightArray >= rightArraySize:
      vector[i] = leftArray[indexLeftArray]
      indexLeftArray += 1  
    elif leftArray[indexLeftArray] < rightArray[indexRightArray]:
      vector[i] = leftArray[indexLeftArray]
      indexLeftArray += 1
      numberOfComparations += 1
    else:
      vector[i] = rightArray[indexRightArray]
      indexRightArray += 1
      numberOfComparations += 1



def mergeSort(vector: list[int], initialIndex: int, finalIndex: int) -> None:
  if initialIndex < finalIndex:
    mid = (initialIndex + finalIndex) // 2
    mergeSort(vector, initialIndex, mid)
    mergeSort(vector, mid + 1, finalIndex)
    merge(vector, initialIndex, mid, finalIndex)

def run(vector: list[int]) -> tuple[list[int], float]:
  vectorCopy = vector[:]

  initialTime = time.time()
  mergeSort(vectorCopy, 0, len(vectorCopy) - 1)
  finalTime = time.time()
  runTime = finalTime - initialTime

  return vectorCopy, runTime

'''
vector = [1, 4, 8, 3, 6, 5, 2, 7]
mergeSort(vector, 0, len(vector) - 1)
for i in vector:
  print(i)
print(numberOfComparations)
'''
