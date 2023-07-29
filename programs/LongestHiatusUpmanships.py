# Heliodex 2022/05/11
# Last edited 2022/11/12 -- cut out a bunch of users to make it faster
# This program takes a long ass time to run compared to all the other ones.

from time import time
from pandas import read_csv


def write(fileRaw: str, outDir: str):
    if not fileRaw:
        return

    table = read_csv(fileRaw, sep="\t")
    out = open(f"{outDir}/LongestHiatusUpmanships.md", "w+", encoding="utf-8")
    longestHiatus = {}
    startTime = time()

    for a in table["author"]:
        if a not in longestHiatus and len(table.query(f"author == '{a}'")) > 1 and a != "[deleted]":
            longestHiatus.update({a: 0})

    for j in longestHiatus:
        # print(j)
        prevComment = 0
        for i in range(len(table)):
            if table["author"][i] == j:
                if not longestHiatus.get(j):
                    longestHiatus.update({j: 1})
                elif longestHiatus[j] < i - prevComment:
                    longestHiatus.update({j: i - prevComment - 1})
                prevComment = i

    longestHiatusCleaned = {}

    for i in longestHiatus:
        if longestHiatus[i] > 0:
            longestHiatusCleaned.update({i: longestHiatus[i]})

    print("took " + str(time() - startTime) + " seconds")

    out.write("**User**|**Longest Hiatus (comments)**\n:-|-:\n")
    out.write(str(sorted(longestHiatusCleaned.items(), key=lambda x: x[1], reverse=True))[
        1:-2].replace("), ", "\n").replace("('", "").replace("', ", "|"))

    out.close()
