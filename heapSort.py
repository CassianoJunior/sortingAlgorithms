# def heapSort(vector: list[int]) -> list[int]:
#   buildMaxHeap(vector)
    
def maxHeapify(vector, i):
    l = 2*i
    r = 2*i+1

    if l <= len(vector) and vector[l] > vector[i]:
        maior = l
    else:
        maior = i
    if r <= len(vector) and vector[r] > vector[maior]:
        maior = r
    if maior != i:
        temp = vector[i]
        vector[i] = vector[maior]
        vector[maior] = temp
        maxHeapify(vector, maior)


# def buildMaxHeap(vector: list[int]):