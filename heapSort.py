
def maxHeapify(vector: list[int], i, tamanhoHeap):
    l = 2*i+1
    r = 2*i+2

    if l < tamanhoHeap and vector[l] > vector[i]:
        maior = l
    else:
        maior = i
    if r < tamanhoHeap and vector[r] > vector[maior]:
        maior = r
    if maior != i:
        temp = vector[i]
        vector[i] = vector[maior]
        vector[maior] = temp
        maxHeapify(vector, maior, tamanhoHeap)

def buildMaxHeap(vector: list[int], tamanhoHeap):
    for i in range((len(vector)//2) - 1, -1, -1):
        maxHeapify(vector, i, tamanhoHeap)

def heapSort(vector: list[int]):
   tamanhoHeap = len(vector)
   buildMaxHeap(vector, tamanhoHeap)
   for i in range(len(vector)-1, -1, -1):
        temp = vector[0]
        vector[0] = vector[i]
        vector[i] = temp
        tamanhoHeap -= 1
        maxHeapify(vector, 0, tamanhoHeap)

v = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heapSort(v)
for i in v:
    print(i)