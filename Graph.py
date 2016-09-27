import pdb
import os


class Graph:
    def __init__(self):
        self.vertices_list = set()
        self.adjacency_dict = {}
        self.status_dict = {}

    def add_edge(self, s_node, d_node):
        self.vertices_list.add(s_node)
        self.vertices_list.add(d_node)
        if not s_node in self.adjacency_dict.keys():
            self.adjacency_dict[s_node] = [d_node]
        else:
            self.adjacency_dict[s_node].append(d_node)



    def BFS(self, s_node):
        BFS_queue = []
        status_dict = {}
        for node in self.vertices_list:
            status_dict[node] = ''

        BFS_queue.append(s_node)

        for node in BFS_queue:
            print(node)
            status_dict[node] = 'Visited'

            try:
                for adj_nodes in self.adjacency_dict[node]:
                    if status_dict[adj_nodes] == '':
                        BFS_queue.append(adj_nodes)

            except:
                pass

    def DFS(self, node):

        status_dict = {}
        for i in self.vertices_list:
            status_dict[i] = ''
        self.DFSUtil(node, status_dict)

    def DFSUtil(self, node, status_dict):
        print(node)
        status_dict[node] = 'Visited'
        try:
            for adj_node in self.adjacency_dict[node]:

                if status_dict[adj_node] == '':
                    self.DFSUtil(adj_node, status_dict)

        except:
            pass

g = Graph()
g.add_edge(a, b, 4)
g.add_edge(a, c, 7)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(3, 6)

g.BFS(1)
g.DFS(1)
