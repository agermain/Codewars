import itertools
def choose_best_sum(t, k, ls):
    combs = list(itertools.combinations(ls,k))
    sums = [i for i in [sum(n) for n in combs] if i<=t]
    if len(sums) == 0:
        return None
    else:
        return max(sums)