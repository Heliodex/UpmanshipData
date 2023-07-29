# Heliodex 2022/04/12
# Last edited 2022/11/06 -- Format output

from pandas import read_csv


def write(fileRaw: str, outDir: str):
    if not fileRaw:
        return

    table = read_csv(fileRaw, sep="\t")

    out = open(f"{outDir}/TotalKarmaGained.md", "w+", encoding="utf-8")

    score = {}

    j = 0
    for i in table["author"]:
        if i in score:
            score.update({i: score.get(i) + table["score"][j]})
        else:
            score.update({i: table["score"][j]})

        j += 1

    out.write("**User**|**Karma gained**\n:-|-:\n")

    for i in sorted(score.items(), key=lambda i: i[1], reverse=True):
        out.write(f"{i[0]}|{i[1]}\n")

    out.close()
