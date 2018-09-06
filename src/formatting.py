from nltk.corpus import stopwords

import logging
import os
import string
import textblob

additional_stopwords = [r"'s", r"n't"]
all_stopwords = set(stopwords.words('english') + additional_stopwords)


#######################
# Writing token lists #
#######################

def createAllTokenLists(directoryPath, blobFunction):
    """
    createAllTokenLists reads all .txt files from data/clean_books, turns each of them
    into a TextBlob, computes a token list by applying `blobFunction` to each blob,
    and then writes each token list as a .csv to `directoryPath`
    """
    for fileName in getTextFiles("data/clean_books"):
        blob = makeBlob(fileName)
        tokenList = blobFunction(blob)
        logging.info(f"Writing {fileName}'s token list to {directoryPath}")
        absoluteFileName = os.path.join(directoryPath, fileName)
        writeTokenList(absoluteFileName, tokenList)

def getTextFiles(directoryPath):
    return [fileName for fileName in os.listdir(directoryPath) if fileName.endswith(".txt") ]

def makeBlob(cleanFileName):
    with open(f"data/clean_books/{cleanFileName}", "r") as cleanFile:
        text = cleanFile.read()
    return textblob.TextBlob(text)

def writeTokenList(absoluteFilePath, tokenList):
    absollutePathNoExt = os.path.splitext(absoluteFilePath)[0]
    with open(f"{absollutePathNoExt}.csv", "w") as destination:
        for token in tokenList:
            destination.write(f"{token}\n")

##################
# Blob functions #
##################

def getAllWords(blob):
    return blob.words

def getNonStopwords(blob):
    return [word for word in blob.words if word.lower() not in all_stopwords]

def getAllTokens(blob):
    return blob.tokens

def getNonStopwordTokens(blob):
    return [token for token in blob.tokens if token.lower() not in all_stopwords]

def getPunctuationOnly(blob):
    allPunctuation = set(string.punctuation)
    return [token for token in blob.tokens if token in allPunctuation]

#########
# Usage #
#########

createAllTokenLists("data/token_lists/without_punctuation/with_stopwords", getAllWords)

createAllTokenLists("data/token_lists/without_punctuation/without_stopwords", getNonStopwords)

createAllTokenLists("data/token_lists/with_punctuation/with_stopwords", getAllTokens)

createAllTokenLists("data/token_lists/with_punctuation/without_stopwords", getNonStopwordTokens)

createAllTokenLists("data/token_lists/just_punctuation", getPunctuationOnly)
