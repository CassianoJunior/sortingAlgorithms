def partition(vector: list[int], firstIndex: int, finalIndex: int):
  pivot = vector[finalIndex]
  previous = firstIndex - 1
  for i in range(firstIndex, finalIndex - 1, -1):
    if vector[i] <= pivot :
      previous += 1
      aux = vector[i]
      vector[i] = vector[previous]
      vector[previous] = aux
  aux = vector[previous + 1]
  vector[previous + 1] = vector[finalIndex]
  vector[finalIndex] = aux

  return previous + 1
 
def quickSort(vector: list[int], firstIndex: int, finalIndex: int):
  if firstIndex < finalIndex:
    pivot = partition(vector, firstIndex, finalIndex)
    quickSort(vector, firstIndex, pivot - 1)
    quickSort(vector, pivot, finalIndex)

testVector = [2, 4, 3, 1, 5]

quickSort(testVector, 0, len(testVector))

for i in range(len(testVector) - 1):
  print(i)