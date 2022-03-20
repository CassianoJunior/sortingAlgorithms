import time

def maxHeapify(vector: list[int], actualNode: int, heapSize: int) -> None:
  leftSon = 2*actualNode+1
  rightSon = 2*actualNode+2

  if leftSon < heapSize and vector[leftSon] > vector[actualNode]:
    largestValue = leftSon
  else:
    largestValue = actualNode
  if rightSon < heapSize and vector[rightSon] > vector[largestValue]:
    largestValue = rightSon
  if largestValue != actualNode:
    aux = vector[actualNode]
    vector[actualNode] = vector[largestValue]
    vector[largestValue] = aux
    maxHeapify(vector, largestValue, heapSize)


def buildMaxHeap(vector: list[int], heapSize: int) -> None:
  for i in range((len(vector)//2) - 1, -1, -1):
    maxHeapify(vector, i, heapSize)


def heapSort(vector: list[int]) -> None:
  heapSize = len(vector)
  buildMaxHeap(vector, heapSize)
  for i in range(len(vector)-1, -1, -1):
    temp = vector[0]
    vector[0] = vector[i]
    vector[i] = temp
    heapSize -= 1
    maxHeapify(vector, 0, heapSize)


def run(vector: list[int]) -> tuple[list[int], float]:
  vectorCopy = vector[:]
  initialTime = time.time()
  heapSort(vectorCopy)
  finalTime = time.time()
  runTime = finalTime - initialTime

  return vectorCopy, runTime
