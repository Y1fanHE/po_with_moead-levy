import numpy as np


def solution(lb, ub):
    x = []
    for l, u in zip(lb, ub):
        xi = np.random.uniform(l, u)
        x += [xi]
    x = np.asarray(x).reshape(len(x), 1)
    s = np.sum(x)
    if s != 0:
        x = x / s
    else:
        print("Repair Error: all components are 0!")
        x = solution(lb, ub)
    return x


def non_constrain(y, lb, ub):
    for i in range(len(y)):
        y[i] = max(y[i], lb[i])
    s = np.sum(y)
    if s != 0:
        y = y / s
    else:
        print("Repair Error: all components are 0!")
        y = solution(lb, ub)
    return y
