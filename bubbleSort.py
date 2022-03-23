import time

numberOfComparations = 0

def bubblesort(vector: list[int]) -> None:
  global numberOfComparations
  for i in range(len(vector)):
    for j in range(len(vector)-1, i, -1):
      numberOfComparations += 1
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

'''
vector = [6, 5, 4, 3, 2, 1]
bubblesort(vector)
for i in vector:
  print(i)
print(numberOfComparations)
'''
