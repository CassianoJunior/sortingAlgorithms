import random
import asyncio

import bubbleSort
import insertionSort
import mergeSort
import heapSort
import quickSort

def showOptions():
  print("""
  Selecione o algoritmo para executar:

  1 - BubbleSort
  2 - InsertionSort
  3 - MergeSort
  4 - HeapSort
  5 - QuickSort

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

async def app():
  print("Gerando vetores...")
  ascendingOrderedVector, descendingOrderedVector, randomVector = await generateVectors("teste.txt")
  print("Vetores gerados!")

  while(True):
    showOptions()
    try:
      option = int(input("Selecione uma opção: "))
    except ValueError:
      print("Digite apenas numeros!")
      continue

    if option == 0: break

    if option == 1:
      print("Option 1")
      

  print("End of program")

asyncio.run(app())