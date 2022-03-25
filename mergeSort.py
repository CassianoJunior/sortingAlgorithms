import timeit

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
    numberOfComparations += 1
    if indexLeftArray >= leftArraySize:
      numberOfComparations += 1
      vector[i] = rightArray[indexRightArray]
      indexRightArray += 1
    elif indexRightArray >= rightArraySize:
      numberOfComparations += 2
      vector[i] = leftArray[indexLeftArray]
      indexLeftArray += 1
    elif leftArray[indexLeftArray] < rightArray[indexRightArray]:
      numberOfComparations += 3
      vector[i] = leftArray[indexLeftArray]
      indexLeftArray += 1
    else:
      numberOfComparations += 3
      vector[i] = rightArray[indexRightArray]
      indexRightArray += 1
  numberOfComparations += 1



def mergeSort(vector: list[int], initialIndex: int, finalIndex: int) -> None:
  global numberOfComparations
  if initialIndex < finalIndex:
    mid = (initialIndex + finalIndex) // 2
    mergeSort(vector, initialIndex, mid)
    mergeSort(vector, mid + 1, finalIndex)
    merge(vector, initialIndex, mid, finalIndex)

  numberOfComparations += 1

def run(vector: list[int]) -> tuple[list[int], float, int]:
  vectorCopy = vector[:]
  runTime = timeit.timeit(lambda: mergeSort(vectorCopy, 0, len(vectorCopy) - 1), number=1)

  return vectorCopy, runTime, numberOfComparations
