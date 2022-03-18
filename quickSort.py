def partition(vector: list[int], firstIndex: int, finalIndex: int) -> int:
  pivot = vector[finalIndex]
  previous = firstIndex - 1
  for i in range(firstIndex, finalIndex):
    if vector[i] <= pivot :
      previous += 1
      aux = vector[i]
      vector[i] = vector[previous]
      vector[previous] = aux

  aux = vector[previous + 1]
  vector[previous + 1] = vector[finalIndex]
  vector[finalIndex] = aux

  return previous + 1
 
def quickSort(vector: list[int], firstIndex: int, finalIndex: int) -> None:
  if firstIndex < finalIndex:
    pivot = partition(vector, firstIndex, finalIndex)
    quickSort(vector, firstIndex, pivot - 1)
    quickSort(vector, pivot, finalIndex)

testVector = [5, 4, 3, 2, 1, 0]

quickSort(testVector, 0, len(testVector) - 1)

for i in testVector:
  print(i)
