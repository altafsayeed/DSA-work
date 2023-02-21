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
    
    def add_edge(self, v1, v2):                         # Add an edge between 2 vertices
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():   # v1 and v2 must BOTH exist in the adj list keys
            self.adj_list[v1].append(v2)                                # At v1 in the list, append v2 to add connection
            self.adj_list[v2].append(v1)                                # At v2 in the list, append v1 to add connection
            return True
        return False
    
    def remove_edge(self, v1, v2):                      # Remove an edge between 2 vertices
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():   # v1 and v2 must BOTH exist in the adj list keys
            try:
                self.adj_list[v1].remove(v2)                                # At v1 in the list, remove v2 to break connection
                self.adj_list[v2].remove(v1)                                # At v2 in the list, remove v1 to break connection
            except ValueError:                  # Ignores value error in the case where an edge between 2 vertices does not exist
                pass
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():          
            for other_vertex in self.adj_list[vertex]:          # Go through list of edges associated with vertex
                self.adj_list[other_vertex].remove(vertex)      # Go to other_vertices and remove edges with vertex we're trying to remove
            del self.adj_list[vertex]                           # Once edges with other vertices are removed, we can delete the vertex
            return True
        return False

    
my_graph = Graph()

my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A','B')
my_graph.add_edge('A','C')
my_graph.add_edge('A','D')
my_graph.add_edge('B','D')
my_graph.add_edge('C','D')

my_graph.remove_vertex('D')

my_graph.print_graph()