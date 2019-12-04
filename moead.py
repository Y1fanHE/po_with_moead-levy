import numpy as np
import pandas as pd
import prob
from nbi_decomp import neighbor
from nbi_decomp import extreme_point
from nbi_decomp import update_extreme
from nbi_decomp import utopia_points
from nbi_decomp import weight_vector
from nbi_decomp import to_update
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
        objs.append(np.array([M, V]))
    return objs


def optimize(instance, N, T, gen, operator, par, sigma, nr, cflag, cgen):
    t, count, temp = 0, 0, 0 # current generation, values used in convergence
    _, r, s, c, lb, ub, port, mp, vp = prob.set(instance) # set up problem
    B = neighbor(N, T) # determine neighbors
    P = population(lb, ub, N) # initialize a population
    objs = objective(P, port, r, s, c) # evaluate objevtives
    F1, F2 = extreme_point(objs) # compute CHIM
    ####################################################################
    indicator_value = igd(objs, mp, vp) # compute IGD metric
    print("{}\t{}".format(t, indicator_value))
    ####################################################################
    while t < gen: # start loop
        for i in range(len(P)): # for every individual
            if np.random.uniform(0,1) < sigma: # decide parent source
                b = B[i] # parent source from neighbor
            else:
                b = np.arange(N) # parent source from whole population
            y = operator(P, i, b, lb, ub, par) # reproduce a offspring
            ############################################################
            # enable this line to compute length of trial vector
            # len_trial = np.linalg.norm(y-P[i])
            ############################################################
            obj_y = objective([y], port, r, s, c)[0] # evaluate offspring
            M_y, V_y = obj_y[0], obj_y[1]
            F1, F2 = update_extreme(obj_y, F1, F2) # update CHIM
            w = weight_vector(F1, F2) # compute normal vector
            Z = utopia_points(N, F1, F2) # compute reference points on CHIM
            update_count = 0 # update limit counter for neighbors
            np.random.shuffle(b) # shuffle parent source
            for bi in b:
                zk = Z[bi]
                obj_k = objs[bi]
                M_k, V_k = obj_k[0], obj_k[1]
                if to_update(M_y, V_y, M_k, V_k, w, zk): # Tchebycheff value
                    P[bi] = y # update to value of offspring
                    objs[bi] = obj_y
                    update_count += 1
                if update_count >= nr: break # break if reached update limit
            ################################################################
            # enable this line to record successfully updated times
            # record_file = open("lvx.csv", "a")
            # record_file.write(f"{t},{len_trial},{update_count}\n")
            ################################################################
        t += 1
        ####################################################################
        # enable this line to save population onjectives during run
        # if t in [0,1,2,3,4,5,10,20,30,50,100,150,200,300]:
        #     pd.DataFrame(objs, columns=["return", "risk"]).to_csv(
        #         f"lvx_pop_gen_{t}.csv", index=False)
        ####################################################################
        indicator_value = igd(objs, mp, vp) # compute IGD metric
        print("{}\t{}".format(t, indicator_value))
        ####################################################################
        if np.abs(indicator_value - temp) >= 1e-05:
            temp = indicator_value
            count = 0
        else:
            count += 1
        if count >= cgen and cflag == True: break # convergence judgement
    return objs
