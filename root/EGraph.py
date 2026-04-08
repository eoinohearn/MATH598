from functions import *

class EGraph():
    def __init__(self, N, P, b, c, w=0.01):
        self.N = N
        self.P = P
        self.b = b
        self.c = c
        self.w = w
        self.graph = gnp_random_connected_graph(N,P)
        self.W, self.k = self.generate()

    def generate(self):
        num_neighbors = [len(self.graph.adj[n]) for n in self.graph.nodes]
        k = np.mean(num_neighbors)
        for node,attributes in self.graph.nodes(data=True):
            attributes['fitness'] = 1
            attributes['strategy'] = 'defect'

        W = np.zeros((self.N,self.N))

        for node in self.graph.adj:
            for nb in self.graph.adj[node]:
                W[node][nb] = 1/self.graph.degree(node)

        r = random.randint(0,self.N-1)
        # print("hello")
        # print("r = ", r)

        self.graph.nodes[r]['strategy'] = 'cooperate'

        return W, k
    
    def calculate_fitness(self):


        for node in self.graph.nodes:
            num_neighbors = len(self.graph.adj[node])
            num_coop = 0
            for nb in self.graph.adj[node]:
                if self.graph.nodes[nb]['strategy'] == 'cooperate':
                    num_coop+=1

            if self.graph.nodes[node]['strategy'] == 'cooperate':
                payoff = self.b*num_coop - self.c*num_neighbors
            else:
                payoff = self.b*num_coop

            self.graph.nodes[node]['fitness'] = 1-self.w + self.w*payoff
            if self.graph.nodes[node]['fitness'] < 0:
                self.graph.nodes[node]['fitness'] = 0
            # print(node,self.graph.nodes[node]['fitness'])


    def update_rule(self):
        
        fitness_values = [self.graph.nodes[n]['fitness'] for n in range(self.N)]
        # print(fitness_values)
        sum_fitness = sum(fitness_values)
        probs = [f/sum_fitness for f in fitness_values]


        selected_node = np.random.choice(self.graph.nodes, p=probs)


        death = np.random.choice(self.graph.nodes, p=self.W[selected_node])

        for key in self.graph.nodes[death].keys():
            self.graph.nodes[death][key] = self.graph.nodes[selected_node][key]
        

    def get_stats(self):

        
        strategies=[self.graph.nodes[n]['strategy'] for n in range(self.N)]

        num_coop = strategies.count('cooperate')
        num_def = strategies.count('defect')

        return num_coop, num_def
    

