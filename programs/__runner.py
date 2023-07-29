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

AllTimesBetween.write(fileRaw, file, outDir)
print("AllTimesBetween done!")

EvenOddRatio.write(fileRaw, file, outDir)
print("EvenOddRatio done!")

FirstAppeareance.write(fileRaw, file, outDir)
print("FirstAppeareance done!")

LastAppearance.write(fileRaw, file, outDir)
print("LastAppearance done!")

LargestPortion.write(fileRaw, file, outDir)
print("LargestPortion done!")

LongestHiatusSeconds.write(fileRaw, file, outDir)
print("LongestHiatusSeconds done!")

LongestHiatusUpmanships.write(fileRaw, file, outDir)
print("LongestHiatusUpmanships done!")

ShortestTimesBetween.write(fileRaw, file, outDir)
print("ShortestTimesBetween done!")

ShortestTimesBetweenX.write(fileRaw, file, outDir)
print("ShortestTimesBetweenX done!")

TotalKarmaGained.write(fileRaw, file, outDir)
print("TotalKarmaGained done!")

TotalUpmanships.write(fileRaw, file, outDir)
print("TotalUpmanships done!")

TotalXUpmanships.write(fileRaw, file, outDir)
print("TotalXUpmanships done!")
