import os
import csv
import collections

def yieldFiles(directoryPath):
    for file in os.listdir(directoryPath):
        yield os.path.join(directoryPath, file)

def yieldLines(filePath):
    with open(filePath, newline="\n") as tsv:
        for line in tsv:
            token, count = line.split("\t")
            yield token, int(count.strip())

def writeFreqDict(directoryPath, outputPath):
    freqDict = collections.defaultdict(int)

    for filePath in yieldFiles(directoryPath):
        for word, count in yieldLines(filePath):
            freqDict[word.lower()] += int(count)

    with open(outputPath, "w") as out:
        for word, count in freqDict.items():
            out.write(f"{word}\t{count}\n")
