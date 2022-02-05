# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 18:14:38 2020

@author: lucijacovic
"""

import networkx as nx
#import timeit

# Vrijeme izvršavanja
# Dijkstra algoritam: oko 0.00275376499999993 / 4.0999999782798115e-07
# Bellman-Ford algoritam: oko 0.0023235539999996034 / 4.020000005766633e-07

# Složenost
# V - broj vrhova, E - broj bridova
# Dijkstra algoritam: O(ElogV)
# Bellman-Ford algoritam: O(EV)

def dijkstra(G):
     return nx.single_source_dijkstra_path(G, 'MAD')
    
def bellamford(G):
    return nx.single_source_bellman_ford_path(G, 'MAD')

def main():
    G = nx.read_pajek('airports−split.net')
    d=dijkstra(G)
    b=bellamford(G)
    print(d,'\n')
    print(b)

if __name__ == "__main__":
    main()


# code_to_test = """
# import networkx as nx
# G = nx.read_pajek('airports−split.net')
# bellamford_path = nx.single_source_bellman_ford_path(G, 'MAD')
# print(bellamford_path)
# """
# elapsed_time = timeit.timeit(code_to_test, number=100)/100
# print (elapsed_time)

#ili

# import timeit
# code_to_test = """
# import networkx as nx
# def dijkstra(G):
#      return nx.single_source_dijkstra_path(G, 'MAD')
# def main():
#     G = nx.read_pajek('airports−split.net')
#     d=dijkstra(G)
#     print(d)
# if __name__ == "__main__":
#     main()
# """
# elapsed_time = timeit.timeit(code_to_test, number=100)/100
# print(elapsed_time)