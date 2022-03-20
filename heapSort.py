
def maxHeapify(vector: list[int], i, heapSize):
    left = 2*i+1
    right = 2*i+2

    if left < heapSize and vector[left] > vector[i]:
        largest = left
    else:
        largest = i
    if right < heapSize and vector[right] > vector[largest]:
        largest = right
    if largest != i:
        aux = vector[i]
        vector[i] = vector[largest]
        vector[largest] = aux
        maxHeapify(vector, largest, heapSize)

def buildMaxHeap(vector: list[int], heapSize):
    for i in range((len(vector)//2) - 1, -1, -1):
        maxHeapify(vector, i, heapSize)

def heapSort(vector: list[int]):
   heapSize = len(vector)
   buildMaxHeap(vector, heapSize)
   for i in range(len(vector)-1, -1, -1):
        temp = vector[0]
        vector[0] = vector[i]
        vector[i] = temp
        heapSize -= 1
        maxHeapify(vector, 0, heapSize)

#v = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
#heapSort(v)
#for i in v:
#   print(i)