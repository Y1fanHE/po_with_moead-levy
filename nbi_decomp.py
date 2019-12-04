import numpy as np


def neighbor(N, t):
    neighbor = []
    for ni in range(N):
        D = []
        for nj in range(N):
            d = np.abs(ni - nj)
            D += [d]
        idx = sorted(np.arange(N), key=lambda x: D[x])
        neighbor += [idx[:int(t)]]
    return neighbor


def extreme_point(obj):
    F1 = min(obj, key=lambda x: x[0])
    F2 = min(obj, key=lambda x: x[1])
    return F1, F2


def update_extreme(obj, F1, F2):
    F1 = min(obj, F1, key=lambda x: x[0])
    F2 = min(obj, F2, key=lambda x: x[1])
    return F1, F2


def weight_vector(F1, F2):
    w1 = np.abs(F1[1] - F2[1])
    w2 = np.abs(F1[0] - F2[0])
    W = np.asarray([w1, w2])
    return W


def utopia_points(N, F1, F2):
    z = []
    for i in range(1, N + 1):
        ai = (N - i) / (N - 1)
        zi = ai * F1 + (1 - ai) * F2
        z += [zi]
    return z



def to_update(M_y, V_y, M_k, V_k, w, zk):
    w1, w2 = w[0], w[1]
    z1, z2 = zk[0], zk[1]
    y1, y2 = M_y, V_y
    k1, k2 = M_k, V_k
    gy = max(w1*(y1-z1), w2*(y2-z2))
    gk = max(w1*(k1-z1), w2*(k2-z2))
    if gy <= gk:
        return True
    else:
        return False
