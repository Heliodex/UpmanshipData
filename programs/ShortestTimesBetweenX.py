# Heliodex 2022/04/12
# Last edited 2022/10/09 -- add loop for files

from pandas import read_csv


def write(fileRaw: str, outDir: str):
    if not fileRaw:
        return

    table = read_csv(fileRaw, sep="\t")

    for x in range(0, 5):
        out = open(f"{outDir}/ShortestTimesBetween{10**x}.md",
                   "w+", encoding="utf-8")

        deltatime = {}

        for i in range(10**x, len(table)):
            deltatime.update(
                {table["id"][i-10**x] + "|" + table["id"][i]: table["timestamp"][i] - table["timestamp"][i-10**x]})

        deltatime = sorted(list(deltatime.items()))
        # print(deltatime)

        for i in range(len(deltatime)):
            deltatime[i] = list(deltatime[i])
            # i no longer like tuples
            deltatime[i][0], deltatime[i][1] = deltatime[i][1], deltatime[i][0]

        deltatime = sorted(deltatime)

        out.write(f"**Starting id**|**Ending id**|**Time (seconds)**\n")
        for i in range(len(deltatime)):
            deltatime[i][0], deltatime[i][1] = deltatime[i][1], deltatime[i][0]
            out.write(f"{deltatime[i][0]}|{deltatime[i][1]}" + "\n")

        out.close()
