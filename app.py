import random
import asyncio
from typing import Callable
from OrdenationExcept import OrdenationExcept

import matplotlib.pyplot as plt

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

  7 - Gerar resultados para amostras pré-definidas

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

async def writeOnFile(fileName: str, ascendingData: tuple[list[int], float, float], descendingData: tuple[list[int], float, float], randomData: tuple[list[int], float, float]) -> None:
  algorithm = fileName.split(".")[0]
  with open(f"data/{fileName}", "w") as file:
    file.write(f"Dados da execucao do algoritmo {algorithm}\n")
    file.write(f"Tempos de ordenacao e comparacoes para os diferentes vetores\n")
    file.write(f"""
  -> Tempo vetor crescente: {ascendingData[0]} | Número de comparações: {ascendingData[1]}\n
  -> Tempo vetor decrescente: {descendingData[0]} | Número de comparações: {descendingData[1]}\n
  -> Tempo vetor aleatório: {randomData[0]} | Número de comparações: {randomData[1]}\n
    """)

def checkOrdenation(vector: list[int], size: int) -> bool:
  for i in range(size):
    if vector[i] != i:
      return False

  return True

def executeAlgorithm(algorithm: Callable[[list[int]], tuple[list[int], float, int]], vectorAscending: list[int], vectorDescending: list[int], randomVector: list[int]) -> tuple[tuple[float, int], tuple[float, int], tuple[float, int]]:
  sumTimeAscendingSortedVector = 0
  sumTimeDescendigSortedVector = 0
  sumTimeRandomVector = 0
  sumComparationsAscendingSortedVector = 0
  sumComparationsDescendingSortedVector = 0
  sumComparationsRandomVector = 0

  for i in range(3):
    orderedVectorForAscending, timeAscending, comparationsAscending = algorithm(vectorAscending)
    sumTimeAscendingSortedVector += timeAscending
    sumComparationsAscendingSortedVector += comparationsAscending
    orderedVectorForDescending, timeDescending, comparationsDescending = algorithm(vectorDescending)
    sumTimeDescendigSortedVector += timeDescending
    sumComparationsDescendingSortedVector += comparationsDescending
    orderedVectorForRandom, timeRandom, comparationsRandom = algorithm(randomVector)
    sumTimeRandomVector += timeRandom
    sumComparationsRandomVector += comparationsRandom

  print("Verificando vetores...")
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
  averageComparationsAscendingSortedVector = sumComparationsAscendingSortedVector / 3
  averageComparationsDescendingSortedVector = sumComparationsDescendingSortedVector / 3
  averageComparationsRandomVector = sumComparationsRandomVector / 3

  dataAscendingVector = [averageTimeAscendingSortedVector, averageComparationsAscendingSortedVector]
  dataDescendingVector = [averageTimeDescendigSortedVector, averageComparationsDescendingSortedVector]
  dataRandomVector = [averageTimeRandomVector, averageComparationsRandomVector]

  return dataAscendingVector, dataDescendingVector, dataRandomVector

def checkSampleIsEmpty(size: int) -> bool:
  return size == 0

def getTimes(times: list[list[float]]) -> tuple[list[float], list[float], list[float]]:
  timesAscending = []
  timesDescending = []
  timesRandom = []
  for time in times:
    timesAscending.append(time[0])
    timesDescending.append(time[1])
    timesRandom.append(time[2])

  return timesAscending, timesDescending, timesRandom

def makeGraph(fileName: str, samples: list[int], times: list[list[float]]):
  timesAscending, timesDescending, timesRandom = getTimes(times)
  plt.figure(figsize=(6, 8))
  plt.xlabel("Tamanho da amostra")
  plt.ylabel("Tempo de ordenação (segundos)")
  plt.title(f"Tempo de ordenação dos diferentes vetores para o\nalgoritmo {fileName} para as amostras")
  plt.xticks(samples, rotation='vertical')
  plt.plot(samples, timesAscending, label="Vetor crescente")
  plt.plot(samples, timesDescending, label="Vetor decrescente")
  plt.plot(samples, timesRandom, label="Vetor aleatório")
  plt.legend()
  plt.savefig(f"graphs/{fileName}.png")
  plt.close()

async def generateData(algorithm: Callable[[list[int]], tuple[list[int], float, int]], ascendingVector: list[int], descendingVector: list[int], fileName: str) -> None:
  samples = [100, 1000, 5000, 30000, 50000, 100000, 150000, 200000]
  samplesForTest = samples[:]
  times = []
  for sample in samplesForTest:
    ascendingVectorTest, descendingVectorTest, randomVectorTest = defineSample(sample, ascendingVector, descendingVector)
    dataAscendingVector, dataDescendingVector, dataRandomVector = executeAlgorithm(algorithm, ascendingVectorTest, descendingVectorTest, randomVectorTest)
    await writeOnFile(f"{fileName}-{sample}.txt", dataAscendingVector, dataDescendingVector, dataRandomVector)
    times.append([dataAscendingVector[0], dataDescendingVector[0], dataRandomVector[0]])

  makeGraph(f"{fileName}", samplesForTest, times)

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

    if option != 7 and option != 6 and checkSampleIsEmpty(sampleSize):
      print("Defina uma amostra antes de executar")
      continue

    if option == 1:
      dataAscendingVector, dataDescendingVector, dataRandomVector = executeAlgorithm(bubbleSort.run, ascendingOrderedVectorTest, descendingOrderedVectorTest, randomVectorTest)

      print("Escrevendo dados...")
      await writeOnFile(f"bubbleSort-{sampleSize}.txt", dataAscendingVector, dataDescendingVector, dataRandomVector)
      print("Verifique o arquivo criado ('bubbleSort.txt') com os dados")

    elif option == 2:
      dataAscendingVector, dataDescendingVector, dataRandomVector = executeAlgorithm(insertionSort.run, ascendingOrderedVectorTest, descendingOrderedVectorTest, randomVectorTest)

      print("Escrevendo dados...")
      await writeOnFile(f"insertionSort-{sampleSize}.txt", dataAscendingVector, dataDescendingVector, dataRandomVector)
      print("Verifique o arquivo criado ('insertionSort.txt') com os dados")

    elif option == 3:
      dataAscendingVector, dataDescendingVector, dataRandomVector = executeAlgorithm(mergeSort.run, ascendingOrderedVectorTest, descendingOrderedVectorTest, randomVectorTest)

      print("Escrevendo dados...")
      await writeOnFile(f"mergeSort-{sampleSize}.txt", dataAscendingVector, dataDescendingVector, dataRandomVector)
      print("Verifique o arquivo criado ('mergeSort.txt') com os dados")

    elif option == 4:
      dataAscendingVector, dataDescendingVector, dataRandomVector = executeAlgorithm(heapSort.run, ascendingOrderedVectorTest, descendingOrderedVectorTest, randomVectorTest)

      print("Escrevendo dados...")
      await writeOnFile(f"heapSort-{sampleSize}.txt", dataAscendingVector, dataDescendingVector, dataRandomVector)
      print("Verifique o arquivo criado ('heapSort.txt') com os dados")

    elif option == 5:
      dataAscendingVector, dataDescendingVector, dataRandomVector = executeAlgorithm(quickSort.run, ascendingOrderedVectorTest, descendingOrderedVectorTest, randomVectorTest)

      print("Escrevendo dados...")
      await writeOnFile(f"quickSort-{sampleSize}.txt", dataAscendingVector, dataDescendingVector, dataRandomVector)
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

    elif option == 7:
      print("""
      Esta opção irá executar todos os algoritmos para os seguintes valores de amostras:
        100,
        1000,
        5000,
        30000,
        50000,
        100000,
        150000,
        200000;
      Além disso, será gerado um arquivo com os dados de cada algoritmo para cada valor de amostra juntamente
      com gráficos para comparação. Isso pode demorar um pouco.
        """)
      answer = input("Deseja continuar? (Sim/Não)\n")
      if answer.lower() != "sim" and answer.lower() != "s": continue

      await generateData(bubbleSort.run, ascendingOrderedVector, descendingOrderedVector, "bubbleSort")
      await generateData(insertionSort.run, ascendingOrderedVector, descendingOrderedVector, "insertionSort")
      await generateData(mergeSort.run, ascendingOrderedVector, descendingOrderedVector, "mergeSort")
      await generateData(heapSort.run, ascendingOrderedVector, descendingOrderedVector, "heapSort")
      await generateData(quickSort.run, ascendingOrderedVector, descendingOrderedVector, "quickSort")
      print("Dados gerados!")
    else:
      print("Digite apenas os valores mostrados.")
      continue

  print("End of program\nBy Abner Brito, Cassiano Junior e José Augusto")

asyncio.run(app())
