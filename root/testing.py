from functions import *
from EGraph import EGraph
import sys


N = 100
# EPOCH = 10000
# k is about equal to Np+2

# p_values = [2/N, 4/N, 6/N, 8/N, 10/N]
P = 6/N
benefit = float(sys.argv[1])

# RATIO = (5,1)
# ratios = [(16,10),(17,10),(18,10),(19,10),(20,10),(21,10),(22,10),(23,10),(24,10)]
          

print("p, k, b/c, n, result")


for _ in range(100000):
    G = EGraph(N,P, benefit, 1)
    n=0
    while(True):
        n+=1
        G.calculate_fitness()
        G.Death_birth()
        x,y = G.get_stats()
        if x == 0:
            break
            
        elif x==N:
            break

        if n>= 100000:
            break


    print(f"{P},{G.k},{benefit}, {n}, {x}")
                



    