import time

numberOfComparations = 0

def bubblesort(vector: list[int]) -> None:
  global numberOfComparations
  for i in range(len(vector)):
    numberOfComparations += 1
    for j in range(len(vector)-1, i, -1):
      numberOfComparations += 1
      if vector[j] < vector[j-1]:
        temp = vector[j]
        vector[j] = vector[j-1]
        vector[j-1] = temp
      numberOfComparations += 1
    numberOfComparations += 1
  numberOfComparations += 1

def run(vector: list[int]) -> tuple[list[int], float, int]:
  vectorCopy = vector[:]
  initialTime = time.time()
  bubblesort(vectorCopy)
  finalTime = time.time()
  runTime = finalTime - initialTime

  return vectorCopy, runTime, numberOfComparations
