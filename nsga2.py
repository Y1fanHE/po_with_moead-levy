import numpy as np
import pandas as pd
import copy
import prob
from domina import fast_non_dominated_sort as fs
from domina import crowding_dist_assignment as cd
from metric import igd


def solution(lb, ub):
    x = []
    for l, u in zip(lb, ub):
        xi = np.random.uniform(l, u)
        x.append(xi)
    x = np.array(x).reshape(len(x), 1)
    s = np.sum(x)
    if s != 0:
        x = x / s
    else:
        x = solution(lb, ub)
    return x


def population(lb, ub, N):
    P = []
    for _ in range(N):
        P.append(solution(lb, ub))
    return P


def objective(P, f, r, s, c):
    objs = []
    for xi in P:
        M, V = f(xi, r, s, c)
        objs.append(np.asarray([M, V]))
    return objs


def optimize(instance, N, gen, operator, par, cflag, cgen):
    t, count, temp = 0, 0, 0
    _, r, s, c, lb, ub, port, mp, vp = prob.set(instance)
    P = population(lb, ub, N) # initialize population
    objs_P = objective(P, port, r, s, c) # evaluate fitness
    ####################################################################
    indicator_value = igd(objs_P, mp, vp) # compute indicator
    print("{}\t{}".format(t, indicator_value))
    ####################################################################
    F, rank = fs(objs_P) # fast non-dominated sorting
    dist = [0] * len(P) # crowding distance assignment
    for Fi in F:
        dist = cd(Fi, objs_P, dist)
    while t < gen: # start generation loop
        Q = operator(P, rank, dist, lb, ub, par) # generate offspring
        objs_Q = objective(Q, port, r, s, c) # compute fitness
        R = P + Q # combine offspring and parent
        objs = objs_P + objs_Q
        F, rank = fs(objs) # fast non-dominated sorting
        dist = [0] * len(R) 
        P_idx, i = [], 0
        while len(P_idx) + len(F[i]) <= N:
            dist = cd(Fi, objs, dist) # crowding distance assignment
            P_idx += F[i] # add front into new population
            i += 1
        dist = cd(F[i], objs, dist)
        Fi = sorted(F[i], key=lambda x: -dist[x]) # sort by distance
        P_idx += Fi[:N-len(P_idx)] # add individuals with large distance
        P, objs_P, tmpRank, tmpDist = [], [], [], []
        for i in P_idx:
            P.append(R[i])
            objs_P.append(objs[i])
            tmpRank.append(rank[i])
            tmpDist.append(dist[i])
        rank = tmpRank
        dist = tmpDist
        t += 1
        ####################################################################
        # enable this line to save population onjectives during run
        # if t in [0,1,2,3,4,5,10,20,30,50,100,150,200,300]:
        #     pd.DataFrame(objs_P, columns=["return", "risk"]).to_csv(
        #         f"nsga2_pop_gen_{t}.csv", index=False)
        ####################################################################
        indicator_value = igd(objs_P, mp, vp) # compute indicator
        print("{}\t{}".format(t, indicator_value))
        ####################################################################
        if np.abs(indicator_value - temp) >= 1e-05: # convergence criteria
            temp = indicator_value
            count = 0
        else:
            count += 1
        if count >= cgen and cflag == True: break
    return objs_P
