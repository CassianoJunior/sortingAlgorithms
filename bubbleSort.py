import time

def bubblesort(vector: list[int]) -> None:
  for i in range(len(vector)):
    for j in range(len(vector)-1, i, -1):
      if vector[j] < vector[j-1]:
        temp = vector[j]
        vector[j] = vector[j-1]
        vector[j-1] = temp

def run(vector: list[int]) -> tuple[list[int], float]:
  vectorCopy = vector[:]
  initialTime = time.time()
  bubblesort(vectorCopy)
  finalTime = time.time()
  runTime = finalTime - initialTime

  return vectorCopy, runTime
