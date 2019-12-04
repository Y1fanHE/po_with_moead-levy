import numpy as np


def transfer_objectives(objs):
    V, M = [], []
    for obji in objs:
        Mi, Vi = obji[0], obji[1]
        M.append(Mi)
        V.append(Vi)
    return M, V


def is_dominated(p, q, M, V):
    Mp, Mq, Vp, Vq = M[p], M[q], V[p], V[q]
    if (Mp < Mq and Vp <= Vq) or (Mp <= Mq and Vp < Vq):
        return 1
    else:
        return 0


def non_dominated(objs):
    M, V = transfer_objectives(objs)
    length = len(M)
    Fi = []
    for p in range(length):
        np = 0
        for q in range(length):
            if is_dominated(q, p, M, V):
                np += 1
        if np == 0:
            Fi.append(p)
    return Fi


def fast_non_dominated_sort(objs):
    M, V = transfer_objectives(objs)
    length = len(M)
    S, n = [], []
    rank = [0] * length
    F, Fi = [], []
    for p in range(length):
        Sp = []
        np = 0
        for q in range(length):
            if is_dominated(p, q, M, V):
                Sp.append(q)
            elif is_dominated(q, p, M, V):
                np += 1
        if np == 0:
            rank[p] = 1
            Fi.append(p)
        S.append(Sp)
        n.append(np)
    F.append(Fi)
    i = 1
    while F[i-1] != []:
        Q = []
        for p in F[i-1]:
            for q in S[p]:
                n[q] -= 1
                if n[q] == 0:
                    rank[q] = i + 1
                    Q.append(q)
        i += 1
        F.append(Q)
    F.remove([])
    return F, rank


def crowding_dist_assignment(Fi, objs, dist):
    M, V = transfer_objectives(objs)
    length = len(Fi)
    for i in Fi:
        dist[i] = 0
    Fi = sorted(Fi, key=lambda x: M[x])
    dist[Fi[0]] = dist[Fi[-1]] = 9999
    for i in range(1, length-1):
        dist[Fi[i]] = dist[Fi[i]] + (np.abs(M[Fi[i+1]] - M[Fi[i-1]])) / (max(M) - min(M))
    Fi = sorted(Fi, key=lambda x: V[x])
    dist[Fi[0]] = dist[Fi[-1]] = 9999
    for i in range(1, length-1):
        dist[Fi[i]] = dist[Fi[i]] + (np.abs(V[Fi[i+1]] - V[Fi[i-1]])) / (max(V) - min(V))
    return dist
