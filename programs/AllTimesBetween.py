# Heliodex 2022/04/12
# Last edited 2022/04/24

import matplotlib
import matplotlib.pyplot as plt
from pandas import read_csv

matplotlib.rcParams['font.family'] = "Readex Pro"


def write(fileRaw: str, outDir: str):
    if not fileRaw:
        return

    table = read_csv(fileRaw, sep="\t")

    out = open(f"{outDir}/AllTimesBetween.txt", "w+", encoding="utf-8")

    deltatime = []

    for i in range(1, len(table)):
        deltatime.append(table["timestamp"][i] - table["timestamp"][i-1])

    # print(deltatime)

    for i in range(len(deltatime)):
        out.write(str(deltatime[i]) + "\n")

    out.close()

    # plt.plot(range(len(deltatime)), deltatime)

    # plt.show()
