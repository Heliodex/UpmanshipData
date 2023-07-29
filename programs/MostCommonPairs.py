# Heliodex 2023/05/14
# Last edited 2023/05/14

from pandas import read_csv


def write(fileRaw: str, outDir: str):
    if not fileRaw:
        return

    table = read_csv(fileRaw, sep="\t")
    out = open(f"{outDir}/MostCommonPairs.md", "w+", encoding="utf-8")

    pairs = {}

    prevAuthor = ""
    for i in range(len(table)):
        a = table["author"][i]
        pair = f"{prevAuthor} {a}"
        if prevAuthor:
            pairs.update({pair: (pairs.get(pair) or 0) + 1})

        prevAuthor = a

    out.write("**Commenter**|**Replied**|**Count**\n:-|:-|-:\n")

    for i in sorted(pairs.items(), key=lambda i: i[1], reverse=True):
        pair = i[0].split(" ")
        out.write(f"{pair[0]}|{pair[1]}|{i[1]}\n")
