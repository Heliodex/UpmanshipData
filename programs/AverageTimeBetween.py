# Heliodex 2022/04/12
# Last edited 2022/11/06 -- Format output

from pandas import read_csv
from statistics import mean


def write(fileRaw: str, outDir: str):
    if not fileRaw:
        return

    table = read_csv(fileRaw, sep="\t")

    deltatime = []

    for i in range(1, len(table)):
        deltatime.append(table["timestamp"][i] - table["timestamp"][i-1])

    print(mean(deltatime))
