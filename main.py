import os
import networkx as nx

def set_of_files(search_path):
    result = {}
    # Wlaking top-down from the root
    for root, _, files in os.walk(search_path):
        for filename in files:
            result[filename] = str(os.path.join(root, filename))
    return result

def look_for_file(filename, file):
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.find(filename)>0:
                return True 

def create_graph(nodes, edges):
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    return G


FILE_PATH = './test'

if __name__ == '__main__':
    edges = set()
    nodes = set_of_files(FILE_PATH)
    for parent, fullpath in nodes.items():
        for child in nodes:
            if look_for_file(child, fullpath):
                edges.add((parent, child))
    graph = create_graph(nodes, edges)
    nx.write_gexf(graph, "./test/test.gexf")
    # print(edges)