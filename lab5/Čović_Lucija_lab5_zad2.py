# citanje csva
import csv
datafile = open('distance.csv', 'r')
datareader = csv.reader(datafile, delimiter=';')
data = []
for row in datareader:
    data.append(row)


# izgradnja matrice iz procitanog csva
gradovi = {}
destinacije = {}
poredak_broken = data[0][0].split(",")
poredak_fixed = poredak_broken[1:]
matrica = data[1:]
for m in matrica:
    info = m[0].split(",")
    grad = info[0]
    udaljenosti = info[1:]
    distance = list(map(lambda x: int(x) if len(x)
                        > 1 else 99999, udaljenosti))
    destinacije = {poredak_fixed[i]: distance[i]
                   for i in range(len(poredak_fixed))}

    gradovi[grad] = destinacije

start = "The Hague"  # grad iz kojeg kreces
n = 3  # broj gradova koji posjecujes


def calculate_lowest():
    next = start
    visited = [start]
    total_distance = 0
    for _ in range(n):
        while True:
            new_city, distance = min(
                gradovi[next].items(), key=lambda x: x[1])
            if new_city not in visited:
                next = new_city
                visited.append(new_city)
                total_distance += distance
                break
            else:
                del gradovi[next][new_city]

    # + gradovi[next][start] jer se vraca na pocetni grad
    return total_distance + gradovi[next][start]


print(calculate_lowest())
