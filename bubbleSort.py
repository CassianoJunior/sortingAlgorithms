def bubblesort(vector: list[int]):
    for i in range(len(vector)):
        for j in range(len(vector)-1, i, -1):
            if vector[j] < vector[j-1]:
                temp = vector[j]
                vector[j] = vector[j-1]
                vector[j-1] = temp

# vector = [5,4,3,2,1,6,8,12,7]
# bubblesort(vector)

# for k in vector:
#     print(k)