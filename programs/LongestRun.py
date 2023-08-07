# Heliodex 2023/05/14
# Last edited 2023/05/14

from pandas import read_csv


def write(fileRaw: str, outDir: str):
    if not fileRaw:
        return

    table = read_csv(fileRaw, sep="\t")
    out = open(f"{outDir}/LongestRun.md", "w+", encoding="utf-8")

    runs = []

    authorsList = []
    runBeginId = ""
    runBeginBody = ""
    runLength = 0

    for i in range(len(table)):
        author = table["author"][i]

        if author not in authorsList:
            if len(authorsList) == 2:
                authorsList = sorted(authorsList, key=str.lower)

                runs.append(authorsList + [[runBeginId, " ".join(runBeginBody.replace("¬n", " ").split(" ")[:2])],
                            [table["id"][i], " ".join(table["body"][i].replace("¬n", " ").split(" ")[:2])], runLength])

                authorsList = []
                runLength = 0
                runBeginId = ""
                runBeginBody = ""

                continue

            authorsList.append(author)

        runLength += 1
        runBeginId = runBeginId or table["id"][i]
        runBeginBody = runBeginBody or table["body"][i]

    out.write(
        "**Users**|**Starting id**|**Ending id**|**Run length**\n:-|:-|:-|-:\n")

    for i in sorted(runs, key=lambda i: i[4], reverse=True):
        out.write(
            f"{i[0]}, {i[1]}|{': '.join(i[2])}|{': '.join(i[3])}|{i[4]}\n")
