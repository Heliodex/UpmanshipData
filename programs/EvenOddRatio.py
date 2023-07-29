# Heliodex 2022/12/10
# Last edited 2022/12/11

from pandas import read_csv


def write(fileRaw: str, file: str, outDir: str):
    table = read_csv(file, sep="\t")

    out = open(f"{outDir}/EvenOddRatio.md", "w+", encoding="utf-8")

    upmanships = {}

    for i in range(len(table)):
        if i == 0:
            continue

        even = False
        if i % 2 == 0:
            even = True

        if table["author"][i] in upmanships:
            prev = upmanships[table["author"][i]]
            if even:
                prev[0] += 1
            else:
                prev[1] += 1

            upmanships.update(
                {table["author"][i]: prev})
        else:
            if even:
                upmanships.update({table["author"][i]: [1, 0]})
            else:
                upmanships.update({table["author"][i]: [0, 1]})

    out.write(
        f"**User**|**Upmanships**|**% of comments with even numbers**\n:-|-:|-:\n")

    for i in sorted(upmanships.items(), key=lambda i: i[1], reverse=True):
        sum = i[1][0] + i[1][1]
        if sum > 1:
            out.write(f"{i[0]}|{sum}|{round(i[1][0] / sum * 100, 1)}\n")
