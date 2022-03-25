import timeit

numberOfComparations = 0

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
    if not j >= 0: numberOfComparations += 1
    if not vector[j] > aux: numberOfComparations += 2
    vector[j+1] = aux
  numberOfComparations += 1

def run(vector: list[int]) -> tuple[list[int], float, int]:
  vectorCopy = vector[:]
  runTime = timeit.timeit(lambda: insertionSort(vectorCopy), number=1)

  return vectorCopy, runTime, numberOfComparations
