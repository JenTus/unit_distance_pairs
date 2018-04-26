"""Import packages."""
import itertools


def choose_2row_3colum(five):
    list_of_two = list(itertools.combinations(five, 2))
    tmp = [[list(set(five).difference(set(two))), two]
           for two in list_of_two]
    return tmp


def create_matrix(list_of_edges, n):
    """
    Given half of all the edges and the number of nodes.

    create the matrix
    """
    matrix = [[0 for i in range(n)] for j in range(n)]
    ind = 0
    for i in range(n):
        for j in range(i):
            matrix[i][j] = list_of_edges[ind]
            matrix[j][i] = list_of_edges[ind]
            ind += 1
    return matrix


def all_matrices(n):
    """Create all the possible adjacency matrices of size n times n."""
    complete = n * (n-1) / 2
    least = (n-1)*2 - 1  # the number of edges is at least 2(n-1)-1
    all_possible_list = [i for i in itertools.product([0, 1], repeat=complete)
                         if sum(i) >= least]
    all_mats = [create_matrix(all_possible_list[i], n) for i in range(n)]
    return all_mats


def check_k23(list_of_mats, n):
    """Return a list of mats that do not contain K23."""
    five_list = list(itertools.combinations([i for i in range(n)], 5))
    check_list = []
    for five in five_list:
        tmp = choose_2row_3colum()
        for tp in tmp:
            check_list.append(tp)
    return check_list
