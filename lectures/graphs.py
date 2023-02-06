class Graph:
    def __init__ (self):
        self.adj_list = {}              # Creating empty adjacency list

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):                   
        if vertex not in self.adj_list.keys():          # If the vertex is not already in the graph (avoid duplicates)
            self.adj_list[vertex] = []                  # Create the vertex and set the value to an empty list (it's not connected to anything yet)
            return True                                 
        return False
    
my_graph = Graph()

my_graph.add_vertex('A')

my_graph.print_graph()