import sys
import numpy as np
import random
import pandas as pd
from dec_reprod import lvx
from moead import optimize


instance = int(sys.argv[1])
rep = 51
benchmarks = ["hangseng", "dax", "ftse", "sp", "nikkei"]
savedir = "tmp/{}/lvx/".format(benchmarks[instance-1])

N, T, gen = 100, 20, 1500
sigma, nr = 0.9, 2
par = [1e-05,0.3]

#print(instance, benchmarks[instance-1])
#print(par)
#print("====================================")

for i in range(rep):
    np.random.seed(500+i)
    random.seed(500+i)
    print("Start {}-th experiment.".format(i+1))
    res = optimize(instance, N, T, gen, lvx, par, sigma, nr, True, 100)
    res = pd.DataFrame(res, columns=["return", "risk"])
    res.to_csv(savedir + str(i+1) + ".csv", index=False)
