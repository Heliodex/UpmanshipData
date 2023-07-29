# Heliodex 2022/10/09
# Last edited 2023/07/29 -- make less awful

import os

import TotalXUpmanships
import TotalUpmanships
import TotalKarmaGained
import ShortestTimesBetweenX
import ShortestTimesBetween
import LongestHiatusUpmanships
import LongestHiatusSeconds
import LargestPortion
import LastAppearance
import FirstAppeareance
import EvenOddRatio
import AllTimesBetween

fileRaw = "./raw30k.tsv"
file = "./30k.tsv"
outDir = "./data"

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
