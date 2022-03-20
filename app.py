import random
import asyncio

import bubbleSort
import insertionSort
import mergeSort
import heapSort
import quickSort

def showOptions():
  print("""
  Selecione uma opcao para executar:

  1 - BubbleSort
  2 - InsertionSort
  3 - MergeSort
  4 - HeapSort
  5 - QuickSort
  6 - Definir tamanho da amostra (max 200000)

  0 - Finalizar o programa
  """)

async def generateVectors(fileName: str) -> tuple[list[int], list[int], list[int]]:
  ascendingOrderedVector = []
  descendingOrderedVector = []
  with open(fileName, 'r') as file:
    data = file.readlines()

  for i in range(len(data)):
    ascendingOrderedVector.append(int(data[i]))
    descendingOrderedVector.append(int(data[len(data) - 1 - i]))

  randomVector = ascendingOrderedVector[:]
  random.shuffle(randomVector)

  return ascendingOrderedVector, descendingOrderedVector, randomVector

def defineSample(sampleSize: int, vectorAscending: list[int], vectorDescending: list[int], randomVector: list[int]) -> tuple[list[int], list[int], list[int]]:
  ascendingOrderedVector = vectorAscending[:sampleSize]
  descendingOrderedVector = vectorDescending[200000-sampleSize:]
  randomArray = randomVector[:sampleSize]

  return ascendingOrderedVector, descendingOrderedVector, randomArray

async def writeOnFile(fileName: str, ascendingData: tuple[list[int], float], descendingData: tuple[list[int], float], randomData: tuple[list[int], float]) -> None:
  algorithm = fileName.split(".")[0]
  with open(fileName, "w") as file:
    file.write(f"Dados da execucao do algoritmo {algorithm}\n")

  with open(fileName, "a") as file:
    file.write(f"Tempo de ordenacao do vetor ordenado crescente: {ascendingData[1]}\n")
    file.write("Vetor ordenado: \n")

  for number in ascendingData[0]:
    with open(fileName, "a") as file:
      file.write(f"{number}\n")

  with open(fileName, "a") as file:
    file.write(f"Tempo de ordenacao do vetor ordenado decrescente: {descendingData[1]}\n")
    file.write("Vetor ordenado: \n")

  for number in descendingData[0]:
    with open(fileName, "a") as file:
      file.write(f"{number}\n")

  with open(fileName, "a") as file:
    file.write(f"Tempo de ordenacao do vetor aleatorio: {randomData[1]}\n")
    file.write("Vetor ordenado: \n")

  for number in randomData[0]:
    with open(fileName, "a") as file:
      file.write(f"{number}\n")

def check(size: int) -> bool:
  return size == 0

async def app():
  print("Gerando vetores...")
  ascendingOrderedVector, descendingOrderedVector, randomVector = await generateVectors("numbers.txt")
  print("Vetores gerados!")

  sampleSize = 0
  ascendingOrderedVectorTest = []
  descendingOrderedVectorTest = []
  randomVectorTest = []

  while(True):
    showOptions()
    try:
      option = int(input("Selecione uma opção: "))
    except ValueError:
      print("Digite apenas numeros!")
      continue

    if option == 0: break

    if option == 1:
      if check(sampleSize):
        print("Defina uma amostra antes de executar")
        continue

      sumTimeAscendingSortedVector = 0
      sumTimeDescendigSortedVector = 0
      sumTimeRandomVector = 0
      for i in range(3):
        orderedVectorForAscending, timeAscending = bubbleSort.run(ascendingOrderedVectorTest)
        sumTimeAscendingSortedVector += timeAscending
        orderedVectorForDescending, timeDescending = bubbleSort.run(descendingOrderedVectorTest)
        sumTimeDescendigSortedVector += timeDescending
        orderedVectorForRandom, timeRandom = bubbleSort.run(randomVectorTest)
        sumTimeRandomVector += timeRandom

      averageTimeAscendingSortedVector = sumTimeAscendingSortedVector / 3
      averageTimeDescendigSortedVector = sumTimeDescendigSortedVector / 3
      averageTimeRandomVector = sumTimeRandomVector / 3

      print("Escrevendo dados...")
      await writeOnFile("bubbleSort.txt", [orderedVectorForAscending, averageTimeAscendingSortedVector], [orderedVectorForDescending, averageTimeDescendigSortedVector], [orderedVectorForRandom, averageTimeRandomVector])
      print("Verifique o arquivo criado ('bubleSort.txt') com os dados")
    elif option == 6:
      size = int(input("Defina o tamanho da amostra para o teste: "))
      ascendingOrderedVectorTest, descendingOrderedVectorTest, randomVectorTest = defineSample(size, ascendingOrderedVector, descendingOrderedVector, randomVector)
      sampleSize = size
      print("Nova amostra definida!")

  print("End of program")

asyncio.run(app())
