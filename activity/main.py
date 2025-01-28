def convert_graph(edge_lst):
    """
    Convert the list of edges to an adjacency matrix.
    Assume the list of edges represents a directed graph.
    """
    # check for the number of nodes in the graph by adding the nodes in the edge list to a set and grabbing the maximum number from that set, adding 1 to account for the 0th index in the matrix
    s = set([node for nodes in edge_lst for node in nodes])

    graph_size = max(s) + 1

    # initialize adjacency matrix with size of graph
    graph = [[0] * graph_size for j in range(graph_size)]

    # set up the connections for each edge in the graph
    for a, b in edge_lst:
        graph[a][b] = 1

    return graph