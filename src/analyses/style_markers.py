from src.analyses import corpus_statistics
import textblob
import os

# before_sun = textblob.TextBlob(corpus_statistics.getAllText("data/hemingway/before_sun")) # words: 35305
# sun = textblob.TextBlob(corpus_statistics.getAllText("data/hemingway/sun")) # words: 69677
# turgenev = textblob.TextBlob(corpus_statistics.getAllText("data/turgenev")) # words: 465766

def writeWordBlocks(inputDirectoryPath, outputDirectoryPath, blockSize):
    wordBlocks = makeWordBlocks(inputDirectoryPath, blockSize)
    for blockNumber, block in enumerate(wordBlocks):
        fileName = f"block{blockNumber}.csv"
        filePath = os.path.join(outputDirectoryPath, fileName)
        writeBlock(filePath, block)

def makeWordBlocks(inputDirectoryPath, blockSize):
    wordList = textblob.TextBlob(corpus_statistics.getAllText(inputDirectoryPath)).words
    return chunkList(wordList, blockSize)

def chunkList(l, chunkSize):
    for index in range(0, len(l), chunkSize):
        yield l[index: index + chunkSize]

def writeBlock(filePath, block):
    with open(filePath, "w") as outputFile:
        for word in block:
            outputFile.write(f"{word}\n")

writeWordBlocks("data/hemingway/before_sun", "data/blocks_size_5000/before_sun", 5000)
