import os
import numpy as np

def get_best(market, alg):
    f = open("../{}/{}/igd.txt".format(market, alg), "r")
    last = ""
    igd_lst = []
    for line in f:
        curr = str(line).rstrip()
        if curr[:5] == "Start" and last != "" and last[0] != "=":
            igd_lst.append(float(last[4:]))
        last = curr
    igd_lst.append(float(last[4:]))
    return np.argmin(igd_lst)+1

markets = ["hangseng", "dax", "ftse", "sp", "nikkei"]
algs = ["de", "dem", "ga", "lvx", "lvxm", "nsga2", "norm", "unif"]
for i, market in enumerate(markets):
    cmd0 = "mkdir ./{}".format(market)
    cmd1 = "mkdir ./{}/final_pop ./{}/igd".format(market, market) # create folders
    os.system(cmd0)
    os.system(cmd1)
    for alg in algs:
        best = get_best(market, alg) # get best runtime no.
        # copy best population file to finasl_pop folder
        cmd2 = "cp ../{}/{}/{}.csv ./{}/final_pop/{}.csv".format(market, alg, best, market, alg)
        os.system(cmd2)

        # copy best igd fraction to igd folder
        f = open("../{}/{}/igd.txt".format(market, alg), "r")
        w = open("./{}/igd/{}.csv".format(market, alg), "a")
        run_no = 0
        igd_frac = []
        for line in f:
            curr = str(line).rstrip()
            if curr[:5] == "Start":
                run_no += 1
            if run_no > best: break
            if run_no == best and curr[:5] != "Start":
                # igd_frac.append(float(curr[4:]))
                w.write(curr+"\n")
        w.close()

    # rename LEVY and CONST
    cmd3 = "cp ./{}/final_pop/lvx.csv ./{}/final_pop/levy.csv".format(market, market)
    cmd4 = "cp ./{}/final_pop/de.csv ./{}/final_pop/const.csv".format(market, market)
    os.system(cmd3)
    os.system(cmd4)
    cmd5 = "cp ./{}/igd/lvx.csv ./{}/igd/levy.csv".format(market, market)
    cmd6 = "cp ./{}/igd/de.csv ./{}/igd/const.csv".format(market, market)
    os.system(cmd5)
    os.system(cmd6)

    # copy portef*.txt
    cmd7 = "cp ./dat/portef{}.txt ./{}/portef.txt".format(i+1, market)
    os.system(cmd7)

