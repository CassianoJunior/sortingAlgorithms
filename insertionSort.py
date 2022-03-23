import time

numberOfComparations = 0

def insertionSort(vector: list[int]) -> None:
  global numberOfComparations
  for i in range(1, len(vector)):
    aux = vector[i]
    j = i-1
    numberOfComparations += 1
    while j >= 0 and vector[j] > aux:
      vector[j+1] = vector[j]
      j -= 1
      numberOfComparations +=1
    vector[j+1] = aux

def run(vector: list[int]) -> tuple[list[int], float]:
  vectorCopy = vector[:]
  initialTime = time.time()
  insertionSort(vectorCopy)
  finalTime = time.time()
  runTime = finalTime - initialTime

  return vectorCopy, runTime

'''
vector = [5, 4, 3, 2 ,1]
insertionSort(vector)
for i in vector:
  print(i)
print(numberOfComparations)  
'''
