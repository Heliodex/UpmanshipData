# Heliodex 2022/04/08
# Last edited 2022/10/29 -- add better output formatting

from pandas import read_csv


def write(file: str, outDir: str):
    if not file:
        return

    table = read_csv(file, sep="\t")

    for x in range(1, 5):
        out = open(f"{outDir}/Total{10**x}Upmanships.md",
                   "w+", encoding="utf-8")

        upmanships = {}

        for i in range(0, len(table), 10**x):
            if i == 0:
                continue
            elif table["author"][i] in upmanships:
                upmanships.update(
                    {table["author"][i]: upmanships[table["author"][i]] + 1})
            else:
                upmanships.update({table["author"][i]: 1})

        out.write(f"**User**|**Milestones**\n:-|-:\n")

        for i in sorted(upmanships.items(), key=lambda i: i[1], reverse=True):
            out.write(f"{i[0]}|{i[1]}\n")
