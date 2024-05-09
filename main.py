import math
from collections import Counter

class DataSet:
    def __init__(self, inx, iny):
        self.x = inx
        self.y = iny

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class DiscreteMaths(DataSet):
    def __init__(self, inx, iny):
        self.x = inx
        self.y = iny

    def euclidean(self, inx, iny, datax, datay):
        return math.sqrt((((inx - datax) ** 2) + ((iny - datay) ** 2)))

    def mean(self, inp):
        return sum(inp) / len(inp)

    def standardDeviation(self, inp):
        vmean = self.mean(inp)
        vlen = len(inp)
        aux = (math.pow(abs((inp[i] - vmean)), 2) for i in range(vlen))
        return math.sqrt((sum(aux)) / (vlen - 1))

class kNearestNeighbor(DiscreteMaths):

    def __init__(self, k = 2):
        self.k = k

    def standardization(self, array, newData):
        vmean = self.mean(array)
        vstanddev = self.standardDeviation(array)
        newList =[(array[i] - vmean) / vstanddev for i in range(len(array))]
        newList.append((newData - vmean) / vstanddev)
        return newList

    def computedDistances(self, xy, new):
        return [self.euclidean(new[0], new[1], i, j) for i, j in xy]

    def findKNearestNeighbor(self, categories, distances):
        listNeighbor = [[i, j] for i, j in zip(categories, distances)]
        sortedList = sorted(listNeighbor, key=lambda x: x[1])
        del sortedList[self.k:]
        count = Counter()

        for i in sortedList:
            count[i[0]] += 1
        category = max(count, key=count.get)
        return category

def calculaKNN(inx, iny):
    k = 5
    altura = [158, 158, 158, 160, 160, 163, 163, 160, 163, 165, 165, 165, 168, 168, 168, 170, 170, 170]
    peso = [58, 59, 63, 59, 60, 60, 61, 64, 64, 61, 62, 65, 62, 63, 66, 63, 64, 68]
    talla = ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L']
    knn = kNearestNeighbor(k)
    heightStand = knn.standardization(altura, inx)
    weightStand = knn.standardization(peso, iny)
    newDataStand = [heightStand.pop(), weightStand.pop()]
    xy = [[i, j] for i, j in zip(heightStand, weightStand)]
    distances = knn.computedDistances(xy, newDataStand)
    res = knn.findKNearestNeighbor(talla, distances)
    print("En base a los valores", inx, "y", iny, "la talla correspondiente seria", res)

print("Implementación de KNN\n")
calculaKNN(174,90)
calculaKNN(183, 70)
calculaKNN(168, 95)
calculaKNN(168, 68)
calculaKNN(153, 60)