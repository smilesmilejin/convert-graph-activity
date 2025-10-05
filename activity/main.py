def convert_graph(edge_lst):
    """
    Convert the list of edges to an adjacency matrix.
    Assume the list of edges represents a directed graph.
    """
    pass

    # fix max number of edge_list
    # matrix will be max * max
    # make them all 0s

    # for each edge
        # make the correponding matrix 1

    # return matrix


    if not edge_lst:
        return []
    

    n = float('-inf')

    for edge in edge_lst:
        n = max(n, max(edge))

    n = n + 1

    matrix = [[0 for j in range(n)] for i in range(n)]
    # print(matrix)

    # matrix = []
    # for i in range(n):
    #     sub = []
    #     for j in range(n):
    #         sub.append(0)

    #     matrix.append(sub)

    print(matrix)

    for row, col in edge_lst:
        # print(row)
        # print(col)
        matrix[row][col] = 1

    return matrix

