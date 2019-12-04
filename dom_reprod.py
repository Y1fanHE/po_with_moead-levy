import numpy as np
from scipy.special import gamma as G
from repair_tool import non_constrain as repair


def ga(P, rank, distances, lb, ub, par):
    pc, pm, etac, etam,  = par[0], par[1], par[2], par[3]
    Q = []
    while len(Q) < len(P):
        p = []
        for _ in range(2):
            idx = np.arange(len(P))
            np.random.shuffle(idx)
            t = idx[:2]
            res = bin_tournament(t, rank, distances)
            p.append(res)
        p1, p2 = P[p[0]], P[p[1]]
        if np.random.uniform(0, 1) <= pc:
            c1, c2 = sbx_crossover(p1, p2, lb, ub, etac)
        else:
            c1, c2 = p1, p2
        c1, c2 = repair(c1, lb, ub), repair(c2, lb, ub)
        c1 = poly_mutation(c1, lb, ub, etam, pm)
        c2 = poly_mutation(c2, lb, ub, etam, pm)
        c1, c2 = repair(c1, lb, ub), repair(c2, lb, ub)
        Q.append(c1)
        Q.append(c2)
    return Q


def bin_tournament(lst, rank, dist):
    a, b = lst[0], lst[1]
    if rank[a] < rank[b]:
        return a
    elif rank[b] < rank[a]:
        return b
    elif dist[a] > dist[b]:
        return a
    else:
        return b


def sbx_crossover(p1, p2, lb, ub, etac):
    c1, c2 = [], []
    for i in range(len(p1)):
        x1 = min(p1[i], p2[i])
        x2 = max(p1[i], p2[i])
        xl, xu = lb[i], ub[i]
        if x2 != x1 and np.random.uniform(0, 1) <= 0.5:
            myu = np.random.uniform(0, 1)
            beta1 = 1 + 2 * (x1-xl) / (x2-x1)
            beta2 = 1 + 2 * (xu-x2) / (x2-x1)
            alpha1 = 2 - beta1 ** (-(etac+1))
            alpha2 = 2 - beta2 ** (-(etac+1))
            if myu <= 1 / alpha1:
                betaq1 = (myu*alpha1) ** (1/(etac+1))
            else:
                betaq1 = (1/(2-myu*alpha1)) ** (1/(etac+1))
            if myu <= 1 / alpha2:
                betaq2 = (myu*alpha2) ** (1/(etac+1))
            else:
                betaq2 = (1/(2-myu*alpha2)) ** (1/(etac+1))
            c1i = 0.5 * ((x1+x2) - betaq1 * (x2-x1))
            c2i = 0.5 * ((x1+x2) + betaq2 * (x2-x1))
            c1i = max(min(c1i, xu), xl)
            c2i = max(min(c2i, xu), xl)
            if np.random.uniform(0, 1) < 0.5:
                c1.append(c1i)
                c2.append(c2i)
            else:
                c1.append(c2i)
                c2.append(c1i)
        else:
            c1.append(x1)
            c2.append(x2)
    c1 = np.array(c1)
    c2 = np.array(c2)
    return c1, c2


def pbm_mutation(p, lb, ub, etam, pm):
    c = []
    for i in range(len(p)):
        x = p[i]
        xl, xu = lb[i], ub[i]
        if np.random.uniform(0, 1) <= pm:
            sigmal = (x-xl) / (xu-xl)
            sigmau = (xu-x) / (xu-xl)
            myu = np.random.uniform(0, 1)
            if myu < 0.5:
                sigmaq = (2*myu + (1-2*myu) * ((1-sigmal)**(etam+1))) ** (1/(etam+1)) - 1
            else:
                sigmaq = 1 - (2*(1-myu) + (2*myu-1) * ((1-sigmau)**(etam+1))) ** (1/(etam+1))
            ci = x + sigmaq * (xu - xl)
        else:
            ci = x
        c.append(ci)
    c = np.array(c)
    return c


def poly_mutation(p, lb, ub, etam, pm):
    for i in range(len(p)):
        if np.random.uniform(0, 1) < pm:
            x = p[i]
            xl, xu = lb[i], ub[i]
            myu = np.random.uniform(0, 1)
            if myu < 0.5:
                sigmaq = (2*myu) ** (1/(etam+1)) - 1
            else:
                sigmaq = 1 - (2*(1-myu)) ** (1/(etam+1))
            p[i] = x + sigmaq * (xu - xl)
    return p
