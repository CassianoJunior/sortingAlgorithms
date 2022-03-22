import random
import asyncio
from OrdenationExcept import OrdenationExcept

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

async def generateVectors(fileName: str) -> tuple[list[int], list[int]]:
  ascendingOrderedVector = []
  descendingOrderedVector = []
  with open(fileName, 'r') as file:
    data = file.readlines()

  for i in range(len(data)):
    ascendingOrderedVector.append(int(data[i]))
    descendingOrderedVector.append(int(data[len(data) - 1 - i]))

  return ascendingOrderedVector, descendingOrderedVector

def defineSample(sampleSize: int, vectorAscending: list[int], vectorDescending: list[int]) -> tuple[list[int], list[int], list[int]]:
  ascendingOrderedVector = vectorAscending[:sampleSize]
  descendingOrderedVector = vectorDescending[200000-sampleSize:]
  randomVector = ascendingOrderedVector[:]
  random.shuffle(randomVector)

  return ascendingOrderedVector, descendingOrderedVector, randomVector

async def writeOnFile(fileName: str, ascendingData: tuple[list[int], float], descendingData: tuple[list[int], float], randomData: tuple[list[int], float]) -> None:
  algorithm = fileName.split(".")[0]
  with open(fileName, "w") as file:
    file.write(f"Dados da execucao do algoritmo {algorithm}\n")
    file.write(f"Tempos de ordenacao para os diferentes vetores\n")

  with open(fileName, "a") as file:
    file.write(f"Tempo vetor crescente: {ascendingData[1]} | Tempo vetor decrescente: {descendingData[1]} | Tempo vetor aleatório: {randomData[1]}\n")
    file.write("Vetor ordenado: \n")

  for numberAscending in ascendingData[0]:
    with open(fileName, "a") as file:
      file.write(f"{numberAscending}\n")

def checkOrdenation(vector: list[int], size: int) -> bool:
  for i in range(size):
    print(vector[i], i)
    if vector[i] != i:
      return False

  return True

def executeAlgorithm(algorithm, vectorAscending: list[int], vectorDescending: list[int], randomVector: list[int]) -> tuple[tuple[list[int], float], tuple[list[int], float], tuple[list[int], float]]:
  sumTimeAscendingSortedVector = 0
  sumTimeDescendigSortedVector = 0
  sumTimeRandomVector = 0

  for i in range(3):
    orderedVectorForAscending, timeAscending = algorithm(vectorAscending)
    sumTimeAscendingSortedVector += timeAscending
    orderedVectorForDescending, timeDescending = algorithm(vectorDescending)
    sumTimeDescendigSortedVector += timeDescending
    orderedVectorForRandom, timeRandom = algorithm(randomVector)
    sumTimeRandomVector += timeRandom

  print("Verificando vetores ordenados...")
  if not checkOrdenation(orderedVectorForAscending, len(vectorAscending)):
    raise OrdenationExcept("Erro na ordenação do vetor ordenado crescente!")

  if not checkOrdenation(orderedVectorForDescending, len(vectorDescending)):
    raise OrdenationExcept("Erro na ordenação do vetor ordenado decrescente!")

  if not checkOrdenation(orderedVectorForRandom, len(randomVector)):
    raise OrdenationExcept("Erro na ordenação do vetor aleatório")
  print("Vetores corretamente ordenados!")

  averageTimeAscendingSortedVector = sumTimeAscendingSortedVector / 3
  averageTimeDescendigSortedVector = sumTimeDescendigSortedVector / 3
  averageTimeRandomVector = sumTimeRandomVector / 3

  dataAscendingVector = [orderedVectorForAscending, averageTimeAscendingSortedVector]
  dataDescendingVector = [orderedVectorForDescending, averageTimeDescendigSortedVector]
  dataRandomVector = [orderedVectorForRandom, averageTimeRandomVector]

  return dataAscendingVector, dataDescendingVector, dataRandomVector

def check(size: int) -> bool:
  return size == 0

async def app():
  print("Gerando vetores...")
  ascendingOrderedVector, descendingOrderedVector = await generateVectors("numbers.txt")
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

    if option != 6 and check(sampleSize):
      print("Defina uma amostra antes de executar")
      continue

    if option == 1:
      dataAscendingVector, dataDescendingVector, dataRandomVector = executeAlgorithm(bubbleSort.run, ascendingOrderedVectorTest, descendingOrderedVectorTest, randomVectorTest)

      print("Escrevendo dados...")
      await writeOnFile("bubbleSort.txt", dataAscendingVector, dataDescendingVector, dataRandomVector)
      print("Verifique o arquivo criado ('bubbleSort.txt') com os dados")

    elif option == 2:
      dataAscendingVector, dataDescendingVector, dataRandomVector = executeAlgorithm(insertionSort.run, ascendingOrderedVectorTest, descendingOrderedVectorTest, randomVectorTest)

      print("Escrevendo dados...")
      await writeOnFile("insertionSort.txt", dataAscendingVector, dataDescendingVector, dataRandomVector)
      print("Verifique o arquivo criado ('insertionSort.txt') com os dados")

    elif option == 3:
      dataAscendingVector, dataDescendingVector, dataRandomVector = executeAlgorithm(mergeSort.run, ascendingOrderedVectorTest, descendingOrderedVectorTest, randomVectorTest)

      print("Escrevendo dados...")
      await writeOnFile("mergeSort.txt", dataAscendingVector, dataDescendingVector, dataRandomVector)
      print("Verifique o arquivo criado ('mergeSort.txt') com os dados")

    elif option == 4:
      dataAscendingVector, dataDescendingVector, dataRandomVector = executeAlgorithm(heapSort.run, ascendingOrderedVectorTest, descendingOrderedVectorTest, randomVectorTest)

      print("Escrevendo dados...")
      await writeOnFile("heapSort.txt", dataAscendingVector, dataDescendingVector, dataRandomVector)
      print("Verifique o arquivo criado ('heapSort.txt') com os dados")

    elif option == 5:
      dataAscendingVector, dataDescendingVector, dataRandomVector = executeAlgorithm(quickSort.run, ascendingOrderedVectorTest, descendingOrderedVectorTest, randomVectorTest)

      print("Escrevendo dados...")
      await writeOnFile("quickSort.txt", dataAscendingVector, dataDescendingVector, dataRandomVector)
      print("Verifique o arquivo criado ('quickSort.txt') com os dados")

    elif option == 6:
      while(True):
        size = int(input("Defina o tamanho da amostra para o teste: "))
        if size <= 200000: break

        print("Digite um valor ate 200000")
        continue

      ascendingOrderedVectorTest, descendingOrderedVectorTest, randomVectorTest = defineSample(size, ascendingOrderedVector, descendingOrderedVector)
      sampleSize = size
      print(f"Nova amostra definida: {size}")

    else:
      print("Digite apenas os valores mostrados.")
      continue

  print("End of program")

asyncio.run(app())
