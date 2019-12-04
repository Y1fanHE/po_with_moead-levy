import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import seaborn as sns


# read igd by generation data
def load_igd(market, alg):
    dat = np.loadtxt("./{}/igd/{}.csv".format(market, alg), delimiter="\t")
    igd = list(dat[:,1])
    while len(igd) < 1501: igd.append(igd[-1])
    dat = {"Generations":list(np.arange(1501)), "IGD":igd}
    dat = pd.DataFrame(dat)
    return dat

# read points in each algorithms solution set
def load_sol(market, alg):
    dat = pd.read_csv("./{}/final_pop/{}.csv".format(market, alg), delimiter=",")
    dat["return"] = -dat["return"]
    return dat

styles = ["paper"]
markets = ["hangseng", "dax", "ftse", "sp", "nikkei"]
xlims = [(0.001,0.0015),(0.0005,0.0008),(0.0003,0.0004),(0.0005,0.001),(0.0004,0.0008)]
ylims = [(0.006,0.008),(0.008,0.009),(0.004,0.006),(0.006,0.008),(0.0015,0.0035)]

# set algorithm names, labels, markers and colors
algs1 = ["lvxm", "dem", "de", "ga", "nsga2"]
algs2 = ["levy", "unif", "norm", "const"]
labs1 = ["MOEA/D-Lévy", "MOEA/D-DEM", "MOEA/D-DE", "MOEA/D-GA", "NSGA-II"]
labs2 = ["LEVY", "UNIF", "NORM", "CONST"]
maks1 = ["o", "v", "^", "s", "D"]
maks2 = ["o", "v", "^", "s"]
cols1 = ["b", "g", "r", "c", "m"]
cols2 = ["b", "g", "r", "c"]

for style in styles:
    if style == "paper":
        font_scale = 1.2
    else:
        font_scale = 1
    # set seaborn style
    sns.set(style, "white", "bright", font_scale=font_scale,
        rc={'font.family': ['sans-serif'],
            'font.sans-serif': ['Arial',
                                'DejaVu Sans',
                                'Liberation Sans',
                                'Bitstream Vera Sans',
                                'sans-serif'],
            'axes.edgecolor': '.0',
            'axes.labelcolor': '.0',
            'text.color': '.0',
            'xtick.bottom': True,
            'xtick.color': '.0',
            'xtick.direction': 'in',
            'xtick.top': True,
            'xtick.major.size': 3,
            'ytick.color': '.0',
            'ytick.direction': 'in',
            'ytick.left': True,
            'ytick.right': True,
            'ytick.major.size': 3,})
    for i, market in enumerate(markets):
        # read points in pareto front
        pf = pd.DataFrame(np.genfromtxt("./{}/portef.txt".format(market)),columns=["return", "risk"])

        dats1 = []
        for alg in algs1:
            dats1.append(load_igd(market, alg))
        dats2= []
        for alg in algs2:
            dats2.append(load_igd(market, alg))

        fig = plt.figure(figsize=(6, 4))
        ax  = fig.add_subplot(1, 1, 1)
        #ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        #ax.ticklabel_format(style="sci",  axis="x",scilimits=(0,0))
        ax.ticklabel_format(style="sci",  axis="y",scilimits=(0,0))
        for dat, mak, col, lab in zip(dats1, maks1, cols1, labs1):
            plt.plot(dat["Generations"], dat["IGD"], label=lab, marker=mak, markevery=200,
                    color=col, markeredgecolor=col, markerfacecolor="none")
        plt.xlabel("Generations")
        plt.ylabel("IGD")
        plt.legend(frameon=True,
                   loc = "upper right",
                   edgecolor="black",
                   fancybox=False)
        plt.savefig("./images/{}_igd1_{}.eps".format(market, style))
        plt.clf()

        #fig = plt.figure(figsize=(6, 4))
        ax  = fig.add_subplot(1, 1, 1)
        #ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        #ax.ticklabel_format(style="sci",  axis="x",scilimits=(0,0))
        ax.ticklabel_format(style="sci",  axis="y",scilimits=(0,0))
        for dat, mak, col, lab in zip(dats2, maks2, cols2, labs2):
            plt.plot(dat["Generations"], dat["IGD"], label=lab, marker=mak, markevery=200,
                    color=col, markeredgecolor=col, markerfacecolor="none")
        plt.xlabel("Generations")
        plt.ylabel("IGD")
        plt.legend(frameon=True,
                   loc = "upper right",
                   edgecolor="black",
                   fancybox=False)
        plt.savefig("./images/{}_igd2_{}.eps".format(market, style))
        plt.clf()

        dats1 = []
        for alg in algs1:
            dats1.append(load_sol(market, alg))
        dats2= []
        for alg in algs2:
            dats2.append(load_sol(market, alg))

        #fig = plt.figure(figsize=(6, 4))
        ax  = fig.add_subplot(1, 1, 1)
        ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        ax.ticklabel_format(style="sci",  axis="x",scilimits=(0,0))
        ax.ticklabel_format(style="sci",  axis="y",scilimits=(0,0))
        plt.plot(pf["risk"], pf["return"], label="Pareto Front", c="black")
        for dat, mak, col, lab in zip(dats1, maks1, cols1, labs1):
            plt.scatter(dat["risk"], dat["return"], label=lab, marker=mak,
                        edgecolors=col, facecolor="none")
        plt.xlabel("Risk")
        plt.ylabel("Return")
        plt.legend(frameon=True,
                   loc = "lower right",
                   edgecolor="black",
                   fancybox=False)
        plt.savefig("./images/{}_pop1_{}.eps".format(market, style))
        plt.clf()

        #fig = plt.figure(figsize=(6, 4))
        ax  = fig.add_subplot(1, 1, 1)
        ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        ax.ticklabel_format(style="sci",  axis="x",scilimits=(0,0))
        ax.ticklabel_format(style="sci",  axis="y",scilimits=(0,0))
        plt.plot(pf["risk"], pf["return"], label="Pareto Front", c="black")
        for dat, mak, col, lab in zip(dats2, maks2, cols2, labs2):
            plt.scatter(dat["risk"], dat["return"], label=lab, marker=mak,
                        edgecolors=col, facecolor="none")
        plt.xlabel("Risk")
        plt.ylabel("Return")
        plt.legend(frameon=True,
                   loc = "lower right",
                   edgecolor="black",
                   fancybox=False)
        plt.savefig("./images/{}_pop2_{}.eps".format(market, style))
        plt.clf()

        #fig = plt.figure(figsize=(6, 4))
        ax  = fig.add_subplot(1, 1, 1)
        ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        ax.ticklabel_format(style="sci",  axis="x",scilimits=(0,0))
        ax.ticklabel_format(style="sci",  axis="y",scilimits=(0,0))
        plt.plot(pf["risk"], pf["return"], label="Pareto Front", c="black")
        for dat, mak, col, lab in zip(dats1, maks1, cols1, labs1):
            plt.scatter(dat["risk"], dat["return"], label=lab, marker=mak,
                        edgecolors=col, facecolor="none")
        plt.xlim(xlims[i])
        plt.ylim(ylims[i])
        plt.xticks([])
        plt.yticks([])
        plt.savefig("./images/{}_pop1scale_{}.eps".format(market, style))
        plt.clf()

        #fig = plt.figure(figsize=(6, 4))
        ax  = fig.add_subplot(1, 1, 1)
        ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        ax.ticklabel_format(style="sci",  axis="x",scilimits=(0,0))
        ax.ticklabel_format(style="sci",  axis="y",scilimits=(0,0))
        plt.plot(pf["risk"], pf["return"], label="Pareto Front", c="black")
        for dat, mak, col, lab in zip(dats2, maks2, cols2, labs2):
            plt.scatter(dat["risk"], dat["return"], label=lab, marker=mak,
                        edgecolors=col, facecolor="none")
        plt.xlim(xlims[i])
        plt.ylim(ylims[i])
        plt.xticks([])
        plt.yticks([])
        plt.savefig("./images/{}_pop2scale_{}.eps".format(market, style))
        plt.clf()
