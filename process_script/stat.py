import numpy as np
import pandas as pd
import sys

markets = ["hangseng", "dax", "ftse", "sp", "nikkei"]
market = markets[int(sys.argv[1])-1]

# read GD data file
dat = pd.read_csv("./num_res/{}.GD.csv".format(market))

# split into two experiments
exp1_GD = dat[dat.columns[:5]]
exp2_GD = dat[dat.columns[5:]]

# calculate statistics
stat1_GD = pd.DataFrame([exp1_GD.min(), exp1_GD.median(), exp1_GD.std()])
stat1_GD.index = ["Best", "Median", "Std."]
stat2_GD = pd.DataFrame([exp2_GD.min(), exp2_GD.median(), exp2_GD.std()])
stat2_GD.index = ["Best", "Median", "Std."]

# find best and second best algorithm
meds1_GD = stat1_GD.loc["Median"].sort_values()
best1_GD = list(meds1_GD.index[:2])
meds2_GD = stat2_GD.loc["Median"].sort_values()
best2_GD = list(meds2_GD.index[:2])

print("{}.GD:".format(market), best1_GD[0], best1_GD[1])
print("{}.GD:".format(market), best2_GD[0], best2_GD[1])

# read Spacing data file
dat = pd.read_csv("./num_res/{}.Spacing.csv".format(market))

# split into two experiments
exp1_Spacing = dat[dat.columns[:5]]
exp2_Spacing = dat[dat.columns[5:]]

# calculate statistics
stat1_Spacing = pd.DataFrame([exp1_Spacing.min(), exp1_Spacing.median(), exp1_Spacing.std()])
stat1_Spacing.index = ["Best", "Median", "Std."]
stat2_Spacing = pd.DataFrame([exp2_Spacing.min(), exp2_Spacing.median(), exp2_Spacing.std()])
stat2_Spacing.index = ["Best", "Median", "Std."]

# find best and second best algorithm
meds1_Spacing = stat1_Spacing.loc["Median"].sort_values()
best1_Spacing = list(meds1_Spacing.index[:2])
meds2_Spacing = stat2_Spacing.loc["Median"].sort_values()
best2_Spacing = list(meds2_Spacing.index[:2])

print("{}.Spacing:".format(market), best1_Spacing[0], best1_Spacing[1])
print("{}.Spacing:".format(market), best2_Spacing[0], best2_Spacing[1])

# read MaxSpread data file
dat = pd.read_csv("./num_res/{}.MaxSpread.csv".format(market))

# split into two experiments
exp1_MaxSpread = dat[dat.columns[:5]]
exp2_MaxSpread = dat[dat.columns[5:]]

# calculate statistics
stat1_MaxSpread = pd.DataFrame([exp1_MaxSpread.max(), exp1_MaxSpread.median(), exp1_MaxSpread.std()])
stat1_MaxSpread.index = ["Best", "Median", "Std."]
stat2_MaxSpread = pd.DataFrame([exp2_MaxSpread.max(), exp2_MaxSpread.median(), exp2_MaxSpread.std()])
stat2_MaxSpread.index = ["Best", "Median", "Std."]

# find best and second best algorithm
meds1_MaxSpread = stat1_MaxSpread.loc["Median"].sort_values(ascending=False)
best1_MaxSpread = list(meds1_MaxSpread.index[:2])
meds2_MaxSpread = stat2_MaxSpread.loc["Median"].sort_values(ascending=False)
best2_MaxSpread = list(meds2_MaxSpread.index[:2])

print("{}.MaxSpread:".format(market), best1_MaxSpread[0], best1_MaxSpread[1])
print("{}.MaxSpread:".format(market), best2_MaxSpread[0], best2_MaxSpread[1])

# read Delta data file
dat = pd.read_csv("./num_res/{}.Delta.csv".format(market))

# split into two experiments
exp1_Delta = dat[dat.columns[:5]]
exp2_Delta = dat[dat.columns[5:]]

# calculate statistics
stat1_Delta = pd.DataFrame([exp1_Delta.min(), exp1_Delta.median(), exp1_Delta.std()])
stat1_Delta.index = ["Best", "Median", "Std."]
stat2_Delta = pd.DataFrame([exp2_Delta.min(), exp2_Delta.median(), exp2_Delta.std()])
stat2_Delta.index = ["Best", "Median", "Std."]

# find best and second best algorithm
meds1_Delta = stat1_Delta.loc["Median"].sort_values()
best1_Delta = list(meds1_Delta.index[:2])
meds2_Delta = stat2_Delta.loc["Median"].sort_values()
best2_Delta = list(meds2_Delta.index[:2])

print("{}.Delta:".format(market), best1_Delta[0], best1_Delta[1])
print("{}.Delta:".format(market), best2_Delta[0], best2_Delta[1])

# read IGD data file
dat = pd.read_csv("./num_res/{}.IGD.csv".format(market))

# split into two experiments
exp1_IGD = dat[dat.columns[:5]]
exp2_IGD = dat[dat.columns[5:]]

# calculate statistics
stat1_IGD = pd.DataFrame([exp1_IGD.min(), exp1_IGD.median(), exp1_IGD.std()])
stat1_IGD.index = ["Best", "Median", "Std."]
stat2_IGD = pd.DataFrame([exp2_IGD.min(), exp2_IGD.median(), exp2_IGD.std()])
stat2_IGD.index = ["Best", "Median", "Std."]

# find best and second best algorithm
meds1_IGD = stat1_IGD.loc["Median"].sort_values()
best1_IGD = list(meds1_IGD.index[:2])
meds2_IGD = stat2_IGD.loc["Median"].sort_values()
best2_IGD = list(meds2_IGD.index[:2])

print("{}.IGD:".format(market), best1_IGD[0], best1_IGD[1])
print("{}.IGD:".format(market), best2_IGD[0], best2_IGD[1])

# read Hypervolume data file
dat = pd.read_csv("./num_res/{}.Hypervolume.csv".format(market))

# split into two experiments
exp1_Hypervolume = dat[dat.columns[:5]]
exp2_Hypervolume = dat[dat.columns[5:]]

# calculate statistics
stat1_Hypervolume = pd.DataFrame([exp1_Hypervolume.max(), exp1_Hypervolume.median(), exp1_Hypervolume.std()])
stat1_Hypervolume.index = ["Best", "Median", "Std."]
stat2_Hypervolume = pd.DataFrame([exp2_Hypervolume.max(), exp2_Hypervolume.median(), exp2_Hypervolume.std()])
stat2_Hypervolume.index = ["Best", "Median", "Std."]

# find best and second best algorithm
meds1_Hypervolume = stat1_Hypervolume.loc["Median"].sort_values(ascending=False)
best1_Hypervolume = list(meds1_Hypervolume.index[:2])
meds2_Hypervolume = stat2_Hypervolume.loc["Median"].sort_values(ascending=False)
best2_Hypervolume = list(meds2_Hypervolume.index[:2])

print("{}.Hypervolume:".format(market), best1_Hypervolume[0], best1_Hypervolume[1])
print("{}.Hypervolume:".format(market), best2_Hypervolume[0], best2_Hypervolume[1])

print("{}\n----------------------------------------------".format(market))
pd.options.display.float_format = '{:.2e}'.format
stat1_overall = pd.concat([stat1_GD, stat1_Spacing, stat1_MaxSpread, stat1_Delta, stat1_IGD, stat1_Hypervolume])
stat2_overall = pd.concat([stat2_GD, stat2_Spacing, stat2_MaxSpread, stat2_Delta, stat2_IGD, stat2_Hypervolume])
arrays = [["GD","GD","GD","Spacing","Spacing","Spacing","MaxSpread","MaxSpread","MaxSpread",
           "Delta","Delta","Delta","IGD","IGD","IGD","Hypervolume","Hypervolume","Hypervolume"],
          stat1_overall.index
         ]
index = pd.MultiIndex.from_arrays(arrays, names=["Metric",""])
stat1_overall.index = index
stat2_overall.index = index
print(stat1_overall)
print("----------------------------------------------")
print(stat2_overall)
