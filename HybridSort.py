import timeit

numberOfComparations = 0

def hybridSort(vector: list[int], initialIndex: int, finalIndex: int) -> None:
    global numberOfComparations
    if isAscendigOrder(vector): 
        insertionSort(vector)
        numberOfComparations += 1
    else: 
        mergeSort(vector, 0, len(vector) - 1)
        numberOfComparations += 1    


def isAscendigOrder(vector: list[int]) -> None:
    global numberOfComparations
    for i in range(1, len(vector)): 
        numberOfComparations += 1
        if vector[i-1] > vector[i]: return False
        numberOfComparations += 1
    numberOfComparations += 1    
    return True    


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

def insertionSort(vector: list[int]) -> None:
  global numberOfComparations
  for i in range(1, len(vector)):
    numberOfComparations += 1
    aux = vector[i]
    j = i-1
    while j >= 0 and vector[j] > aux:
      numberOfComparations += 2
      vector[j+1] = vector[j]
      j -= 1
    if not j >= 0:
        numberOfComparations += 1
    if not vector[j] > aux:
        numberOfComparations += 2
    vector[j+1] = aux
  numberOfComparations += 1

    