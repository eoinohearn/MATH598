import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random
import itertools


def gnp_random_connected_graph(n, p):
    """
    Generates a random undirected graph, similarly to an Erdős-Rényi 
    graph, but enforcing that the resulting graph is conneted
    """
    edges = itertools.combinations(range(n), 2)
    G = nx.Graph()
    G.add_nodes_from(range(n))
    if p <= 0:
        return G
    if p >= 1:
        return nx.complete_graph(n, create_using=G)
    for _, node_edges in itertools.groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < p:
                G.add_edge(*e)
    return G


def calculate_fitness(graph,b,c,w):


    for node in graph.nodes:
        num_neighbors = len(graph.adj[node])
        num_coop = 0
        for nb in graph.adj[node]:
            if graph.nodes[nb]['strategy'] == 'cooperate':
                num_coop+=1

        if graph.nodes[node]['strategy'] == 'cooperate':
            payoff = b*num_coop - c*num_neighbors
            if payoff < 0:
                payoff =0
        else:
            payoff = b*num_coop
        graph.nodes[node]['fitness'] = 1-w+w*payoff



def update_rule(graph, W):
    
    N = len(graph.nodes)
    fitness_values = [graph.nodes[n]['fitness'] for n in range(N)]
    
    sum_fitness = sum(fitness_values)
    probs = [f/sum_fitness for f in fitness_values]


    selected_node = np.random.choice(graph.nodes, p=probs)


    death = np.random.choice(graph.nodes, p=W[selected_node])

    for key in graph.nodes[death].keys():
        graph.nodes[death][key] = graph.nodes[selected_node][key]
    
    return graph


def get_stats(graph):

    N = len(graph.nodes)
    strategies=[graph.nodes[n]['strategy'] for n in range(N)]

    num_coop = strategies.count('cooperate')
    num_def = strategies.count('defect')

    return num_coop, num_def

def create_graph(N,p):

    graph = gnp_random_connected_graph(N,p)

    num_neighbors = [len(graph.adj[n]) for n in graph.nodes]
    k = np.mean(num_neighbors)
    for node,attributes in graph.nodes(data=True):
        attributes['fitness'] = 1
        attributes['strategy'] = 'defect'

    W = np.zeros((N,N))

    for node in graph.adj:
        for nb in graph.adj[node]:
            W[node][nb] = 1/graph.degree(node)

    r = random.randint(0,N-1)

    graph.nodes[r]['strategy'] = 'cooperate'

    return graph, W, k