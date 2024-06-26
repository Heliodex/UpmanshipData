# Heliodex 2022/10/09
# Last edited 2023/07/29 -- make less awful

import os
from time import time

import TotalXUpmanships
import TotalUpmanships
import TotalKarmaGained
import ShortestTimesBetweenX
import ShortestTimesBetween
import LongestHiatusSeconds
import LongestHiatusUpmanships
import LongestRun
import LargestPortion
import LastAppearance
import FirstAppeareance
import EvenOddRatio
import AllTimesBetween

fileRaw = "./other/oneupmanshipRaw.tsv"
file = "./other/oneupmanship.tsv"
outDir = "./data"

start = time()

if not os.path.exists(outDir):
    os.makedirs(outDir)

AllTimesBetween.write(fileRaw, outDir)
print("AllTimesBetween done!")

EvenOddRatio.write(file, outDir)
print("EvenOddRatio done!")

FirstAppeareance.write(fileRaw, outDir)
print("FirstAppeareance done!")

LastAppearance.write(fileRaw, outDir)
print("LastAppearance done!")

LargestPortion.write(fileRaw, outDir)
print("LargestPortion done!")

LongestHiatusSeconds.write(fileRaw, outDir)
print("LongestHiatusSeconds done!")

LongestHiatusUpmanships.write(fileRaw, outDir)
print("LongestHiatusUpmanships done!")

LongestRun.write(fileRaw, outDir)
print("LongestRun done!")

ShortestTimesBetween.write(fileRaw, outDir)
print("ShortestTimesBetween done!")

ShortestTimesBetweenX.write(fileRaw, outDir)
print("ShortestTimesBetweenX done!")

TotalKarmaGained.write(fileRaw, outDir)
print("TotalKarmaGained done!")

TotalUpmanships.write(fileRaw, outDir)
print("TotalUpmanships done!")

TotalXUpmanships.write(file, outDir)
print("TotalXUpmanships done!")

print(f"Time to complete: {str(time() - start)} seconds")
