import numpy as np
from scipy.special import gamma as G
from repair_tool import non_constrain as repair


def ga(P, i, b, lb, ub, par):
    pc, pm, etac, etam = par[0], par[1], par[2], par[3]
    np.random.shuffle(b)
    p1, p2 = P[b[0]], P[b[1]]
    if np.random.uniform(0, 1) < pc:
        c1, c2 = sbx_crossover(p1, p2, lb, ub, etac)
    else:
        c1, c2 = p1, p2
    if np.random.uniform(0, 1) < 0.5:
        y = c1
    else:
        y = c2
    y = repair(y, lb, ub)
    y = poly_mutation(y, lb, ub, etam, pm)
    y = repair(y, lb, ub)
    return y


def de(P, i, b, lb, ub, par):
    f = par[0]
    np.random.shuffle(b)
    p1 = P[i]
    p2, p3 = P[b[0]], P[b[1]]
    y = p1 + f * (p2 - p3)
    y = repair(y, lb, ub)
    return y


def de_uniform(P, i, b, lb, ub, par):
    f = par[0]
    np.random.shuffle(b)
    p1 = P[i]
    p2, p3 = P[b[0]], P[b[1]]
    y = np.zeros((len(p1), 1))
    for j in range(len(p1)):
        y[j] = p1[j] + np.random.uniform(-f,f) * (p2[j] - p3[j])
    y = repair(y, lb, ub)
    return y


def de_normal(P, i, b, lb, ub, par):
    f = par[0]
    np.random.shuffle(b)
    p1 = P[i]
    p2, p3 = P[b[0]], P[b[1]]
    y = np.zeros((len(p1), 1))
    for j in range(len(p1)):
        y[j] = p1[j] + f * np.random.normal(1) * (p2[j] - p3[j])
    y = repair(y, lb, ub)
    return y


def dem(P, i, b, lb, ub, par):
    f, pm, etam = par[0], par[1], par[2]
    np.random.shuffle(b)
    p1 = P[i]
    p2, p3 = P[b[0]], P[b[1]]
    y = p1 + f * (p2 - p3)
    y = repair(y, lb, ub)
    y = poly_mutation(y, lb, ub, etam, pm)
    y = repair(y, lb, ub)
    return y


def lvxm(P, i, b, lb, ub, par):
    alpha, beta, pm, etam = par[0], par[1], par[2], par[3]
    np.random.shuffle(b)
    p1 = P[i]
    p2 = P[b[0]]
    y = p1 + alpha * levy(beta, len(p1)) * (p1 - p2)
    y = repair(y, lb, ub)
    y = poly_mutation(y, lb, ub, etam, pm)
    y = repair(y, lb, ub)
    return y


def lvx(P, i, b, lb, ub, par):
    alpha, beta = par[0], par[1]
    np.random.shuffle(b)
    p1 = P[i]
    p2 = P[b[0]]
    y = p1 + alpha * levy(beta, len(p1)) * (p1 - p2)
    y = repair(y, lb, ub)
    return y


def sbx_crossover(p1, p2, lb, ub, etac):
    c1, c2 = [], []
    for i in range(len(p1)):
        x1 = min(p1[i], p2[i])
        x2 = max(p1[i], p2[i])
        xl, xu = lb[i], ub[i]
        if np.random.uniform(0, 1) < 0.5:
            if x1 != x2:
                myu = np.random.uniform(0, 1)
                beta1 = 1 + 2 * (x1-xl) / (x2-x1)
                beta2 = 1 + 2 * (xu-x2) / (x2-x1)
                alpha1 = 2 - beta1 ** (-(etac+1))
                alpha2 = 2 - beta2 ** (-(etac+1))
                if myu <= 1 / alpha1:
                    betaq1 = (myu*alpha1) ** (1/(etac+1))
                else:
                    betaq1 = (1/(2-myu*alpha1)) ** \
                    (1/(etac+1))
                if myu <= 1 / alpha2:
                    betaq2 = (myu*alpha2) ** (1/(etac+1))
                else:
                    betaq2 = (1/(2-myu*alpha2)) ** \
                    (1/(etac+1))
                c1i = 0.5 * ((x1+x2) - betaq1 * (x2-x1))
                c2i = 0.5 * ((x1+x2) + betaq2 * (x2-x1))
                c1.append(c1i)
                c2.append(c2i)
            else:
                c1.append(x1)
                c2.append(x2)
        else:
            c1.append(x1)
            c2.append(x2)
    c1, c2 = np.array(c1).reshape(len(c1), 1), np.array(c2).reshape(len(c2), 1)
    return c1, c2


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


def levy(beta, n):
    num = G(1+beta) * np.sin(np.pi*beta/2)
    den = G((1+beta)/2) * beta * 2**((beta-1)/2)
    sigma_u, sigma_v = (num/den) ** (1/beta), 1
    u, v = np.random.normal(0, sigma_u, size=n), \
    np.random.normal(0, sigma_v, size=n)
    z = u/(np.abs(v)**(1/beta))
    return z.reshape(n,1)
