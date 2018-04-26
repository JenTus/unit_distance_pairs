import itertools
import time
from check_forbidden_patterns import check_k23, check_k4, all_matrices


def get_possible_mats(n):
    all_mats = all_matrices(n)
    temp1 = check_k23(all_mats, n)
    result = check_k4(temp1, n)
    return result


for n in range(4, 10):
    start_time = time.time()
    res = get_possible_mats(n)
    mx = [sum([sum(j) for j in i]) for i in res]
    print "when n is %d the largest edges is %d\n" % (n, int(max(mx)/2))
    m = max(mx)
    print "there are %d cases\n" % len([i for i, j in enumerate(mx) if j == m])
    print "for example\n"
    print res[mx.index(max(mx))]
