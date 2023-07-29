# Heliodex 2022/04/08
# Last edited 2022/12/11 -- Format output even bettrer
# i accidentally deleted this program, also fix nans

import matplotlib
import matplotlib.pyplot as plt
from pandas import read_csv

matplotlib.rcParams["text.color"] = "w"
matplotlib.rcParams["savefig.facecolor"] = "k"


def write(fileRaw: str, outDir: str):
    if not fileRaw:
        return

    table = read_csv(fileRaw, sep="\t")

    out = open(f"{outDir}/TotalUpmanships.md", "w+", encoding="utf-8")

    upmanships = {}

    for i in range(len(table)):
        if i == "[deleted]":
            # print("whoOOPs")
            continue
        elif table["author"][i] in upmanships:
            upmanships.update(
                {table["author"][i]: upmanships[table["author"][i]] + 1})
        else:
            upmanships.update({table["author"][i]: 1})

    out.write("**User**|**Upmanships**\n:-|-:\n")

    for i in sorted(upmanships.items(), key=lambda i: i[1], reverse=True):
        out.write(f"{i[0]}|{i[1]}\n")

    # plt.pie(sorted(list(upmanships.values()), reverse=True),
    #		 labels=list([f"{i}, {upmanships[i]}" for i in sorted(
    #					 upmanships, key=upmanships.__getitem__, reverse=True)]),
    #		 startangle=90)
    # plt.show()
