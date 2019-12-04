import numpy as np
import pandas as pd


def read_file(prob_num):
    df = pd.read_csv("dat/port" + str(prob_num) + ".txt", header=None,
    delimiter="\s+", names=range(3)) # info on assets
    n = int(df[0][0]) # number of assets
    r = df[1: (n + 1)][0].values.reshape(n, 1) # mean of returns
    s = df[1: (n + 1)][1].values.reshape(n, 1) # std. of returns
    df = df.values
    c = np.zeros((n, n))
    for it in np.arange(n,len(df)):
        i, j = int(df[it][0] - 1), int(df[it][1] - 1)
        c[i][j] = c[j][i] = df[it][2] # covariance between asset i, j
    return n, r, s, c


def evaluate(x, r, s, c):
    M = - np.sum(np.dot(x.T, r)) # obj. 1: -1 * mean as return
    V = np.sum(np.dot(x, x.T) * np.dot(s, s.T) * c) # obj. 2: variance as risk
    return M, V


def pf(prob_num):
    pf = np.genfromtxt("dat/portef" + str(prob_num) + ".txt") # points on pf
    M = []
    V = []
    for i in range(len(pf)):
        M += [pf[i][0]]
        V += [pf[i][1]]
    return M, V


def set(instance):
    n, r, s, c = read_file(instance)
    lb, ub = np.zeros((n, 1)), np.ones((n, 1)) # upper and lower bounds
    port = evaluate
    mp, vp = pf(instance)
    return n, r, s, c, lb, ub, port, mp, vp
