import timeit
import insertionSort
import mergeSort

numberOfComparations = 0
globalOrderedVector = []

def isAscendingOrder(vector: list[int]) -> bool:
  global numberOfComparations
  for i in range(1, len(vector)):
    numberOfComparations += 1
    if vector[i-1] > vector[i]:
      numberOfComparations += 1
      return False
    numberOfComparations += 1
  numberOfComparations += 1
  return True

def hybridSort(vector: list[int]) -> None:
  global numberOfComparations
  global globalOrderedVector
  if isAscendingOrder(vector):
    orderedVector, runtime, comparations = insertionSort.run(vector)
  else:
    orderedVector, runtime, comparations = mergeSort.run(vector)

  numberOfComparations += 1 + comparations
  globalOrderedVector = orderedVector[:]


def run(vector: list[int]) -> tuple[list[int], float, int]:
  runTime = timeit.timeit(lambda: hybridSort(vector), number=1)

  return globalOrderedVector, runTime, numberOfComparations
