from src.analyses import corpus_statistics
from src import csv_utilities
import textblob
import os
import statistics
import scipy.stats

########################
# Creating Word Blocks #
########################

def writeWordBlocks(inputDirectoryPath, outputDirectoryPath, blockSize):
    wordBlocks = makeWordBlocks(inputDirectoryPath, blockSize)
    for blockNumber, block in enumerate(wordBlocks):
        fileName = f"block{blockNumber}.csv"
        filePath = os.path.join(outputDirectoryPath, fileName)
        writeBlock(filePath, block)

def makeWordBlocks(inputDirectoryPath, blockSize):
    wordList = textblob.TextBlob(corpus_statistics.getAllText(inputDirectoryPath)).words
    return chunkList(wordList, blockSize)

def makeSentenceBlocks(inputDirectoryPath, blockSize):
    text = textblob.TextBlob(corpus_statistics.getAllText(inputDirectoryPath))
    sentenceBlocks = list()
    nextBlock = list()
    wordsAdded = 0
    for sentence in text.sentences:
        if wordsAdded >= blockSize:
            sentenceBlocks.append(nextBlock)
            nextBlock = list()
            wordsAdded = 0
        else:
            nextBlock.append(sentence)
            wordsAdded += len(sentence.words)
    return sentenceBlocks

def chunkList(l, chunkSize):
    for index in range(0, len(l), chunkSize):
        yield l[index: index + chunkSize]

########################
# Word Block Utilities #
#######################

def writeBlock(filePath, block):
    with open(filePath, "w") as outputFile:
        for word in block:
            outputFile.write(f"{word}\n")

def readBlock(blockPath):
    with open(blockPath, "r") as blockFile:
        return blockFile.read().split("\n")

def readAllBlocks(directoryPath):
    return [ readBlock( os.path.join( directoryPath, fileName ) ) for fileName in csv_utilities.listCSVFiles(directoryPath) ]

####################
# Block Statistics #
####################

def computeBlockStatistics(directoryPath, statisticFunction):
    for block in readAllBlocks(directoryPath):
        yield statisticFunction(block)

def averageWordLength(block):
    return sum( map(len,block) ) / len(block)

def averageUniqueWordLength(block):
    uniqueWords = set(block)
    return sum( map(len, uniqueWords) ) / len(uniqueWords)

def averageSentenceLength(sentenceBlocks):
    for sentenceBlock in sentenceBlocks:
        yield sum( len(sentence.words) for sentence in sentenceBlock ) / len(sentenceBlock)

def writeBlockStatistics(outputPath, blockStatistics):
    with open(outputPath, "w") as outputFile:
        for stat in blockStatistics:
            outputFile.write(f"{stat}\n")

######################
# Summary Statistics #
######################

def summarizeBlockStatistics(statisticPath):
        stats = readBlockStatistics(statisticPath)
        average = statistics.mean(stats)
        stdev = statistics.stdev(stats, xbar=average)
        return average, stdev

def readBlockStatistics(statisticsPath):
    with open(statisticsPath, "r") as statisticsFile:
        stats = statisticsFile.read().split("\n")[:-1]
        return list(map(float, stats))
