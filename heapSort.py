import timeit

numberOfComparations = 0

def maxHeapify(vector: list[int], actualNode: int, heapSize: int) -> None:
  global numberOfComparations
  leftSon = 2*actualNode+1
  rightSon = 2*actualNode+2

  if leftSon < heapSize and vector[leftSon] > vector[actualNode]:
    largestValue = leftSon
    numberOfComparations += 2
  else:
    largestValue = actualNode
    if not leftSon < heapSize:
      numberOfComparations += 1
    else:
      if not vector[leftSon] > vector[actualNode]: numberOfComparations += 2

  if rightSon < heapSize and vector[rightSon] > vector[largestValue]:
    largestValue = rightSon
    numberOfComparations += 2
  else:
    print(rightSon, heapSize)
    if not rightSon < heapSize:
      numberOfComparations += 1
    else:
      if not vector[rightSon] > vector[largestValue]: numberOfComparations += 2

  if largestValue != actualNode:
    aux = vector[actualNode]
    vector[actualNode] = vector[largestValue]
    vector[largestValue] = aux
    maxHeapify(vector, largestValue, heapSize)
  numberOfComparations += 1


def buildMaxHeap(vector: list[int], heapSize: int) -> None:
  global numberOfComparations
  for i in range((len(vector)//2) - 1, -1, -1):
    numberOfComparations += 1
    maxHeapify(vector, i, heapSize)
  numberOfComparations += 1


def heapSort(vector: list[int]) -> None:
  global numberOfComparations
  heapSize = len(vector)
  buildMaxHeap(vector, heapSize)
  for i in range(len(vector)-1, -1, -1):
    numberOfComparations += 1
    temp = vector[0]
    vector[0] = vector[i]
    vector[i] = temp
    heapSize -= 1
    maxHeapify(vector, 0, heapSize)
  numberOfComparations += 1


def run(vector: list[int]) -> tuple[list[int], float, int]:
  vectorCopy = vector[:]
  runTime = timeit.timeit(lambda: heapSort(vectorCopy), number=1)

  return vectorCopy, runTime, numberOfComparations
