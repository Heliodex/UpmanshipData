# Heliodex 2022/04/12
# Last edited 2022/11/06
# Made it no longer loop through the

from pandas import read_csv


def write(fileRaw: str, file: str, outDir: str):
    table = read_csv(fileRaw, sep="\t")

    out = open(f"{outDir}/FirstAppearance.md", "w+", encoding="utf-8")

    firstappearance = {}

    for i in range(len(table)):
        t = [
            table["timestamp"][i],
            table["body"][i], table["id"][i]]

        try:
            for j in firstappearance:
                if j[1] == t[1] or t[1] == "[deleted]":
                    raise  # probably a better way to go about this
        except:
            continue

        if table["author"][i] not in firstappearance:
            firstappearance.update({table["author"][i]: t})

    out.write("**User**|**First comment**|**Id**\n:-|:-|:-\n")

    for i, v in sorted(firstappearance.items(), key=lambda i: i[1][0]):
        out.write(f"{i}|{v[1]}|{v[2]}\n")

    out.close()
