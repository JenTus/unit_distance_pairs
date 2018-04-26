import itertools
import time
from check_forbidden_patterns import check_k23, check_k4, all_matrices


def get_possible_mats(n):
    all_mats = all_matrices(n)
    temp1 = check_k23(all_mats, n)
    result = check_k4(temp1, n)
    return result


start_time = time.time()
res = get_possible_mats(7)
print res
print "%s seconds" % (time.time() - start_time)
