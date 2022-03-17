def insertionSort(vector):
    for i in range(1, len(vector)):
        aux = vector[i]
        j = i-1
        while j >= 0 and vector[j] > aux:
            vector[j+1] = vector[j]
            j -= 1
        vector[j+1] = aux    

vector = [5,4,2,3,1]
insertionSort(vector)
for i in vector:
    print(i)        