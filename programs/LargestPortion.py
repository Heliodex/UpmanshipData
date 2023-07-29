# Heliodex 2022/11/12
# Last edited 2022/11/12

from pandas import read_csv


def write(fileRaw: str, file: str, outDir: str):
    table = read_csv(fileRaw, sep="\t")
    out = open(f"{outDir}/LargestPortion.md", "w+", encoding="utf-8")

    upmanships = {}
    largestPortion = {}

    for a in table["author"]:
        if a not in upmanships:
            upmanships.update({a: 0})
            largestPortion.update({a: [0, 0]})

    for i in range(0, len(table)):
        author = table["author"][i]
        if author in upmanships:
            upmanships.update(
                {author: upmanships[author] + 1})

            portion = upmanships[author] / (i + 1)
            if portion > largestPortion[author][0]:
                largestPortion.update({author: [portion, i + 1]})

        else:
            upmanships.update({table["author"][i]: 1})

    out.write("**User**|**Largest percentage**|**Point achieved**\n:-|-:|-:\n")

    for i in sorted(largestPortion.items(), key=lambda i: i[1], reverse=True):
        out.write(f"{i[0]}|{round(i[1][0] * 100, 2)}%|{i[1][1]}\n")
