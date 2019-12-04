import sys
import numpy as np
import random
import pandas as pd
from dom_reprod import ga
from nsga2 import optimize


instance = int(sys.argv[1])
rep = 51
benchmarks = ["hangseng", "dax", "ftse", "sp", "nikkei"]
savedir = "tmp/{}/nsga2/".format(benchmarks[instance-1])

N, T, gen = 100, 20, 1500
par = [0.7,0.01,20,20]

#print(instance, benchmarks[instance-1])
#print(par)
#print("====================================")

for i in range(rep):
    np.random.seed(500+i)
    random.seed(500+i)
    print("Start {}-th experiment.".format(i+1))
    res = optimize(instance, N, gen, ga, par, True, 100)
    res = pd.DataFrame(res, columns=["return", "risk"])
    res.to_csv(savedir + str(i+1) + ".csv", index=False)
