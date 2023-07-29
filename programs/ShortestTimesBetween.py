# Heliodex 2022/04/12
# Last edited 2022/11/06 -- Format output

from pandas import read_csv


def write(fileRaw: str, file: str, outDir: str):
    table = read_csv(fileRaw, sep="\t")

    out = open(f"{outDir}/ShortestTimesBetween.md", "w+", encoding="utf-8")

    deltatime = {}

    for i in range(1, len(table)):
        if table["author"][i] == "[deleted]" or table["author"][i] not in deltatime or deltatime[table["author"][i]][0] > int(table["timestamp"][i] - table["timestamp"][i-1]):
            deltatime.update(
                {table["author"][i]: [table["timestamp"][i] - table["timestamp"][i-1], table["id"][i]]})

    deltatime = sorted(list(deltatime.items()))
    # print(deltatime)

    for i in range(len(deltatime)):
        deltatime[i] = list(deltatime[i])
        # i no longer like tuples
        deltatime[i][0], deltatime[i][1] = deltatime[i][1], deltatime[i][0]

    deltatime = sorted(deltatime)

    out.write("|**Username**|**Fastest time (seconds)**|**Comment ID**|\n:-|-:|:-\n")

    for i in range(len(deltatime)):
        deltatime[i][0], deltatime[i][1] = deltatime[i][1], deltatime[i][0]
        out.write(
            f"{deltatime[i][0]}|{deltatime[i][1][0]}|{deltatime[i][1][1]}\n")

    out.close()
