from functions import *
from EGraph import EGraph


N = 100
EPOCH = 10000
# k is about equal to Np+2

# p_values = [2/N, 4/N, 6/N, 8/N, 10/N]
P = 2/N
RATIO = (5,1)
# ratios = [(16,10),(17,10),(18,10),(19,10),(20,10),(21,10),(22,10),(23,10),(24,10)]
          

print("p, k, b/c, n, result")


for _ in range(10000):
    G = EGraph(N,P, RATIO[0], RATIO[1])
    length=EPOCH
    for n in range(EPOCH):
        G.calculate_fitness()
        G.update_rule()
        x,y = G.get_stats()
        if x == 0:
            length=n
            break
            
        elif x==N:
            length=n
            break


    print(f"{P},{G.k},{RATIO[0]/RATIO[1]}, {length}, {x}")
                



    