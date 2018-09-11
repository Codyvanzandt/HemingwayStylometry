from src import formatting, csv_utilities
import itertools
import collections
import os
import textblob
from hyphen import Hyphenator


def computeTextStatistics(inputDirectoryPath, outputFilePath, blobFunction):
    allText = textblob.TextBlob(getAllText(inputDirectoryPath))
    statistics = blobFunction(allText)
    formatting.writeTokenList(outputFilePath, statistics)

def getAllText(directoryPath):
    allText = str()
    for fileName in os.listdir(directoryPath):
        with open(os.path.join(directoryPath, fileName), "r") as f:
            allText += f.read()
            allText += "\n"
    return allText

def mostCommonFactory(start, end):
    def mostCommon(blob):
        wordList = [word.lower() for word in blob.words if "'" not in word]
        frequency = collections.Counter(wordList)
        return [ f"{word},{token}" for word, token in frequency.most_common(end)[start:] ]
    return mostCommon

# most_common_100_function = mostCommonFactory(0, 100)
# computeTextStatistics("data/token_lists/without_punctuation/with_stopwords", "data/analysis_results/reading_list/100_most_common.csv", most_common_100_function)
# computeTextStatistics("data/hemingway/sun", "data/analysis_results/sun/100_most_common.csv", most_common_100_function)
# computeTextStatistics("data/hemingway/before_sun", "data/analysis_results/before_sun/100_most_common.csv", most_common_100_function)

# most_common_1000_to_2000_function = mostCommonFactory(1000, 2000)
# computeTextStatistics("data/token_lists/without_punctuation/with_stopwords", "data/analysis_results/reading_list/1000_to_2000_most_common.csv", most_common_1000_to_2000_function)
# computeTextStatistics("data/hemingway/sun", "data/analysis_results/sun/1000_to_2000_most_common.csv", most_common_1000_to_2000_function)
# computeTextStatistics("data/hemingway/before_sun", "data/analysis_results/before_sun/1000_to_2000_most_common.csv", most_common_1000_to_2000_function)

# h_en = Hyphenator('en_US')
# h_en.syllables('beautiful')
