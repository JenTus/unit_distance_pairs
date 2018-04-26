"""Import packages"""
import itertools


def create_matrix(list_of_edges, n):
    """
    Given half of all the edges and the number of nodes.
    create the matrix
    """
    matrix = [[0 for i in range(n)] for j in range(n)]
    ind = 0
    for i in range(n):
        for j in range(i+1):
            matrix[i][j] = list_of_edges[ind]
            matrix[j][i] = list_of_edges[ind]
            ind += 1
    return matrix


def all_matrices(n):
    """Create all the possible adjacency matrices of size n times n."""
    complete = n * (n-1) / 2
    least = (n-1)*2 - 1  # the number of edges is at least 2(n-1)-1
    all_possible_list = [i for i in itertools.product([0, 1], repeat=complete)
                         if sum(i) >= total_ones]


def check_k23
