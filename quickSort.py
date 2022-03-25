import timeit

numberOfComparations = 0

def quickSort(vector: list[int], firstIndex: int, finalIndex: int) -> None:
  global numberOfComparations
  startIndex = firstIndex
  endIndex = finalIndex
  pivot = vector[(firstIndex + finalIndex) // 2]

  while startIndex <= endIndex:
    numberOfComparations += 1
    while vector[startIndex] < pivot:
      startIndex += 1
      numberOfComparations += 1
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

  numberOfComparations += 1

  if firstIndex < endIndex:
    quickSort(vector, firstIndex, endIndex)
  numberOfComparations += 1
  if finalIndex > startIndex:
    quickSort(vector, startIndex, finalIndex)
  numberOfComparations += 1

def run(vector: list[int]) -> tuple[list[int], float, int]:
  vectorCopy = vector[:]
  runTime = timeit.timeit(lambda: quickSort(vectorCopy, 0, len(vectorCopy)-1), number=1)

  return vectorCopy, runTime, numberOfComparations



