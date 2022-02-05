# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 16:01:38 2020

@author: lucijacovic
"""

import networkx as nx
import math


# Napomena:
    
# Isprike na groznom kodu, iskreno nisam znala drugačije riješit.
# Za A* je sve zakomentirano jer uporno imam isti error koji sam vam bila poslala na chatu,
# možda vi znate do čega je? "NetworkXNotImplemented: not implemented for multigraph type"
# Na intenetu ne piše ništa meni razumljivo za taj error.


# Vrijeme izvršavanja
# Greedy Best-first Search algoritam: "SyntaxError: EOL while scanning string literal" - opet ne znam do čega je, svi su strinogvi zatvoreni s navodnicima
# A* algoritam: error

# Složenost
# V - broj vrhova, E - broj bridova
# Greedy Best-first Search algoritam: O(V+E)
# A* algoritam: error

def greedy(G, source, target, visited, queue):
    visited.append(source)
    queue.append(source)

    while queue: #dok queue nije prazan
        s = queue.pop(0) #makni prvi vrh iz liste
        if s==target: #ako je trenutni jednak cilju
            break
        print (s, end = " ")
    
        for neighbour in G[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    print(target) #ne vata target za ispis
    
# def astar(G, source, target, heu):
#     return nx.astar_path(G, source, target, heu)

# def heu(G, source, target):
#     if (source == 'LHR'):
#         x1=1085
#         y1=1500
#     if (source == 'BER'):
#         x1=2015
#         y1=1580
#     if (source == 'MAD'):
#         x1=590
#         y1=300
#     if (source == 'KPB'):
#         x1=3225
#         y1=1515
#     if (source == 'FCO'):
#         x1=2010
#         y1=355
#     if (source == 'CDG'):
#         x1=1225
#         y1=1170
#     if (source == 'MSQ'):
#         x1=2900
#         y1=1880
#     if (source == 'ARN'):
#         x1=2240
#         y1=2415
#     if (source == 'DUB'):
#         x1=730
#         y1=1830
#     if (source == 'VIE'):
#         x1=2265
#         y1=1075
#     if (target == 'LHR'):
#         x2=1085
#         y2=1500
#     if (target == 'BER'):
#         x2=2015
#         y2=1580
#     if (target == 'MAD'):
#         x2=590
#         y2=300
#     if (target == 'KPB'):
#         x2=3225
#         y2=1515
#     if (target == 'FCO'):
#         x2=2010
#         y2=355
#     if (target == 'CDG'):
#         x2=1225
#         y2=1170
#     if (target == 'MSQ'):
#         x2=2900
#         y2=1880
#     if (target == 'ARN'):
#         x2=2240
#         y2=2415
#     if (target == 'DUB'):
#         x2=730
#         y2=1830
#     if (target == 'VIE'):
#         x2=2265
#         y2=1075
#     a=(x2-x1)**2+(y2-y1)**2
#     a=abs(a)
#     dist=math.sqrt(a)
#     return dist

def main():
    G = nx.read_pajek('airports-astar.net')
    # nisam znala preko pajeka za greedy...
    G2 = { 
      'MAD' : ['CDG','FCO'],
      'CDG' : ['BER', 'FCO', 'LHR'],
      'FCO' : ['VIE'],
      'LHR' : ['DUB', 'ARN'],
      'DUB' : [],
      'BER' : ['ARN', 'MSQ', 'VIE'],
      'VIE' : ['KPB'],
      'ARN' : ['MSQ'],
      'KPB' : ['MSQ'],
      'MSQ' : []
    }
    source = input('Unesi prvi aerodrom:')
    target = input('Unesi drugi aerodrom:')
    visited=[]
    queue=[]
    print("\nGreedy BFS:")
    greedy(G2, source, target, visited, queue)
    # h=heu(G, source, target)
    # a=astar(G, source, target, h)
    print("\nA*:")
    # print(a)

if __name__ == "__main__":
    main()


# import timeit
# code_to_test = """
# def greedy(G, source, target, visited, queue):
#     visited.append(source)
#     queue.append(source)

#     while queue: #dok queue nije prazan
#         s = queue.pop(0) #makni prvi vrh iz liste
#         if s==target: #ako je trenutni jednak cilju
#             break
#         print (s, end = " ") #end je space
    
#         for neighbour in G[s]:
#             if neighbour not in visited:
#                 visited.append(neighbour)
#                 queue.append(neighbour)
#     print(target)
# def main():
#     G = nx.read_pajek('airports-astar.net')
#     G2 = {
#       'MAD' : ['CDG','FCO'],
#       'CDG' : ['BER', 'FCO', 'LHR'],
#       'FCO' : ['VIE'],
#       'LHR' : ['DUB', 'ARN'],
#       'DUB' : [],
#       'BER' : ['ARN', 'MSQ', 'VIE'],
#       'VIE' : ['KPB'],
#       'ARN' : ['MSQ'],
#       'KPB' : ['MSQ'],
#       'MSQ' : []
#     }
#     source = input('Unesi prvi aerodrom:')
#     target = input('Unesi drugi aerodrom:')
#     visited=[]
#     queue=[]
#     print("\nGreedy BFS:")
#     greedy(G2, source, target, visited, queue)
#     # h=heu(G, source, target)
#     # a=astar(G, source, target, h)
#     print("\nA*:")
#     # print(a)
# if __name__ == "__main__":
#     main()
# """
# elapsed_time = timeit.timeit(code_to_test, number=100)/100
# print(elapsed_time)

