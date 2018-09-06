import os
import csv
import itertools

def loadAllCSVFiles(directoryPath):
    return {fileName: loadCSVData(directoryPath, fileName) for fileName in listCSVFiles(directoryPath)}

def loadCSVData(directoryPath, csvFileName):
    absolutePath = os.path.join(directoryPath, csvFileName)
    with open(absolutePath, "r") as csvFile:
        csvData = list(itertools.chain.from_iterable(csv.reader(csvFile)))
    return csvData

def listCSVFiles(directoryPath):
    return [fileName for fileName in os.listdir(directoryPath) if fileName.endswith(".csv") ]
