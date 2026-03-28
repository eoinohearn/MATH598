import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


class Individual():
    
    def __init__(self, fitness=1):
        self.fitness = fitness

# create graph, random, star, simple, line, ....
graph = nx.stochastic_graph(nx.gnp_random_graph(15,0.10, directed=True))
print(graph)

nx.draw(graph, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1200)

# 3. Display the plot
plt.title("Simple NetworkX Graph")
plt.show()