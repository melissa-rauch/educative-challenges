from linkedlist import LinkedList

class Graph:
    def __init__(self, vertices):

        # total number of vertices
        self.vertices = vertices

        # Defining a list which can hold multiple Linked Lists
        # equal to the number of vertices in the graph
        self.array = []

        for i in range(vertices):
            temp = LinkedList()
            self.array.append(temp)

    # method to add an edge from source to destination, Time complexity = O(1)
    def add_edge(self, source, dest):
        if(source < self.vertices and dest < self.vertices):
            self.array[source].insert_at_head(dest)
            # Uncomment the following line for an undirected graph:
            # self.array[dest].insert_at_head(source)

    # method to print the content of a graph, time complexity = O(n^2)?
    def print_graph(self):

        print(">>Adjacency List of Directed Graph<<")
        print
        # for each vertex
        for i in range(self.vertices):
            # print the vertex
            print("|", i, end=" | => ")
            #set a temp variable to the head of that LL
            temp = self.array[i].get_head()
            #while there is a head
            while(temp is not None):
                #pring the temp data
                print("[", temp.data, end=" ] -> ")
                #set temp to next node
                temp = temp.next_element
            #once at the end, print None
            print("None")
    
    # method 
    