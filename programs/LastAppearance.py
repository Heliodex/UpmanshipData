# Heliodex 2022/04/12
# Last edited 2022/04/24

from pandas import read_csv


def write(fileRaw: str, file: str, outDir: str):
    table = read_csv(fileRaw, sep="\t")

    out = open(f"{outDir}/LastAppearance.md", "w+", encoding="utf-8")

    lastappearance = {}

    for i in range(len(table)):
        t = [
            table["timestamp"][i],
            table["body"][i], table["id"][i]]

        lastappearance.update({table["author"][i]: t})

    out.write("**User**|**Last comment**|**Id**\n:-|:-|:-\n")

    for i, v in sorted(lastappearance.items(), key=lambda i: i[1][0]):
        out.write(f"{i}|{v[1]}|{v[2]}\n")

    out.close()
