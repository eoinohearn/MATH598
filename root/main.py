from functions import *



N = 100
EPOCH = 1000
# k is about equal to Np+2

# p_values = [2/N, 4/N, 6/N, 8/N, 10/N]
P = 2/N
RATIO = (240,10)
# ratios = [(16,10),(17,10),(18,10),(19,10),(20,10),(21,10),(22,10),(23,10),(24,10)]
          




with open(f"results{P}.txt", "w") as file:
    file.write("p, k, b/c, n, result\n")
    for _ in range(10):
        graph, W, k = create_graph(N, P)
        result = "inconclusive"
        length=EPOCH
        for n in range(EPOCH):
            calculate_fitness(graph, RATIO[0],RATIO[1], 0.01)
            update_rule(graph, W)
            x,y = get_stats(graph)
            
            if x == 0:
                result = "extinct"
                length=n
                
            elif x==N:
                result = "fixation"
                length=n

        if _ % 10 == 0:
            print("running")

            
        file.write(f"{P},{k},{RATIO[0]/RATIO[1]}, {length}, {result}\n")
                



    