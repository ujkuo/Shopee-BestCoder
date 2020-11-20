
class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node
        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


if __name__ == "__main__":
    V = 5
    
    # Create graph and edges
     
    graph = Graph(V)
    output = []
    list1 = [(1,4),(2,5),(4,6),(6,7)]
    print(len(list1))
    count = 0
    for item in list1:
        i0 = item[0]
        i1 = item[1]
        for j in range(len(list1)):
            if j != count:
                if(i1 == list1[j][0])
        #graph.add_edge(item[0], item[1])
        #print(item)
    print(output)

    #graph.print_agraph()
