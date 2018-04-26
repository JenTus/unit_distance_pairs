"""Import packages."""
import itertools


def choose_2row_3colum(five):
    """Choose 2 as rows and 3 as colums from 5 given numbers."""
    list_of_two = list(itertools.combinations(five, 2))
    tmp = [[list(two), list(set(five).difference(set(two)))]
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
    complete = int(n * (n-1) / 2)
    least = (n-1)*2 - 1  # the number of edges is at least 2(n-1)-1
    all_possible_list = [i for i in itertools.product([0, 1], repeat=complete)
                         if sum(i) >= least]
    all_mats = [create_matrix(i, n) for i in all_possible_list]
    return all_mats


def check_k23(list_of_mats, n):
    """Return a list of mats that do not contain K23."""
    five_list = list(itertools.combinations([i for i in range(n)], 5))
    check_list = []
    possible_mats = []
    for five in five_list:
        tmp = choose_2row_3colum(five)
        for tp in tmp:
            check_list.append(tp)
    for mats in list_of_mats:
        flag = 0
        for ttp in check_list:
            [rrow, ccolum] = ttp
            if sum([mats[row][colum] for row in rrow for colum in ccolum]) == 6:
                flag = 1
                break
        if flag == 0:
            possible_mats.append(mats)
    return possible_mats


def check_k4(list_of_mats, n):
    """Return a list of mats that do not contain K4."""
    four_list = list(itertools.combinations([i for i in range(n)], 4))
    coordinate_list = [list(itertools.combinations(four, 2)) for four in four_list]
    possible_mats = []
    for mats in list_of_mats:
        flag = 0
        for coordinate in coordinate_list:
            if sum([mats[cor[0]][cor[1]] for cor in coordinate]) == 6:
                flag = 1
                break
        if flag == 0:
            possible_mats.append(mats)
    return possible_mats
