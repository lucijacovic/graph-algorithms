import csv
from itertools import permutations

# citanje csva
datafile = open('distance.csv', 'r')
datareader = csv.reader(datafile, delimiter=';')
data = []
matrix = []
for row in datareader:
    data.append(row)
matrica = data[1:]
for m in matrica:
    info = m[0].split(",")
    udaljenosti = info[1:]
    distance = list(map(lambda x: int(x) if len(x)
                        > 1 else 0, udaljenosti))
    matrix.append(distance)

broj_gradova = len(matrix[0])

permu = permutations(range(broj_gradova))


def calculate_lowest(broj_gradova):
    udaljenosti = []
    matrica = matrix
    while permu:
        current = next(permu)
        zbroj = 0
        for i in range(len(current) - 1):
            zbroj = matrica[current[i]][current[i+1]] + zbroj
        zbroj = matrica[current[-1]][current[0]] + zbroj
        udaljenosti.append(zbroj)

    return min(udaljenosti)


print(calculate_lowest(broj_gradova))
