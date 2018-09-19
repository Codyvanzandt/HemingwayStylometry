from src import formatting, csv_utilities
import itertools
import collections
import os
import textblob
import statistics
from nltk.stem.porter import PorterStemmer
from text_matcher import matcher

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

def posDistribution(blob):
    posTags = [tag for token, tag in blob.tags]
    numberTokens = len(posTags)
    posCounter = collections.Counter(posTags)
    return [ f"{tag},{count},{count/numberTokens}" for tag, count in posCounter.most_common() ]

def nGramFactory(n, tokenType):
    def nGram(blob):
        tokenList = [ tag for _, tag in blob.tags ] if tokenType == "POS" else blob.words
        ngrams = list(zip(*[tokenList[i:] for i in range(n)])) # clever solution via locallyoptimal.com
        numberNGrams = len(ngrams)
        nGramCounter = collections.Counter(ngrams)
        return [ f"{ngram},{count},{count/numberNGrams}" for ngram, count in nGramCounter.most_common() ]
    return nGram

def yulesK(blob):
    d = collections.defaultdict(int)
    stemmer = PorterStemmer()
    stemmedWords = map(lambda w: stemmer.stem(w).lower(), blob.words)
    stemmedCounts = collections.Counter(stemmedWords)

    M1 = len(stemmedCounts.values())
    M2 = sum([len(list(g))*(freq**2) for freq,g in itertools.groupby(sorted(stemmedCounts.values()))])

    try:
        return [ f"{10000*(M2-M1)/(M1**2)}" ]
    except ZeroDivisionError:
        return [ "0" ]

def hapax_legomena_percentage(blob):
    wordList = blob.words
    numberWords = len(wordList)
    wordCounter = collections.Counter(blob.words)
    numberHapaxLegomena = sum(1 for numUses in wordCounter.values() if numUses== 1)
    return [ f"{numberHapaxLegomena/numberWords}" ]

def average_sentence_length(blob):
    sentences = blob.sentences
    numberSentences = len(sentences)
    sentenceLengths = [ len(sentence.words) for sentence in sentences ]
    averageLength = sum(sentenceLengths) / numberSentences
    lengthStdev = statistics.stdev(sentenceLengths, xbar=averageLength)
    return [ f"{averageLength,lengthStdev}" ]



# most_common_100_function = mostCommonFactory(0, 100)
# computeTextStatistics("data/hemingway/sun", "data/analysis_results/sun/100_most_common.csv", most_common_100_function)
# computeTextStatistics("data/hemingway/before_sun", "data/analysis_results/before_sun/100_most_common.csv", most_common_100_function)
# computeTextStatistics("data/token_lists/without_punctuation/with_stopwords", "data/analysis_results/reading_list/100_most_common.csv", most_common_100_function)

# most_common_1000_to_2000_function = mostCommonFactory(1000, 2000)
# computeTextStatistics("data/hemingway/sun", "data/analysis_results/sun/1000_to_2000_most_common.csv", most_common_1000_to_2000_function)
# computeTextStatistics("data/hemingway/before_sun", "data/analysis_results/before_sun/1000_to_2000_most_common.csv", most_common_1000_to_2000_function)
# computeTextStatistics("data/token_lists/without_punctuation/with_stopwords", "data/analysis_results/reading_list/1000_to_2000_most_common.csv", most_common_1000_to_2000_function)

# computeTextStatistics("data/hemingway/sun", "data/analysis_results/sun/pos_distribution.csv", posDistribution)
# computeTextStatistics("data/hemingway/before_sun", "data/analysis_results/before_sun/pos_distribution.csv", posDistribution)
# computeTextStatistics("data/token_lists/without_punctuation/with_stopwords", "data/analysis_results/reading_list/pos_distribution.csv", posDistribution)

# pos_3gram_function = nGramFactory(3,"POS")
# computeTextStatistics("data/hemingway/sun", "data/analysis_results/sun/pos_3grams.csv", pos_3gram_function)
# computeTextStatistics("data/hemingway/before_sun", "data/analysis_results/before_sun/pos_3grams.csv", pos_3gram_function)
# computeTextStatistics("data/token_lists/without_punctuation/with_stopwords", "data/analysis_results/reading_list/pos_3grams.csv", pos_3gram_function)

# word_3gram_function = nGramFactory(3,"WORD")
# computeTextStatistics("data/hemingway/sun", "data/analysis_results/sun/word_3grams.csv", word_3gram_function)
# computeTextStatistics("data/hemingway/before_sun", "data/analysis_results/before_sun/word_3grams.csv", word_3gram_function)
# computeTextStatistics("data/token_lists/without_punctuation/with_stopwords", "data/analysis_results/reading_list/word_3grams.csv", word_3gram_function)

# computeTextStatistics("data/hemingway/sun", "data/analysis_results/sun/yules_k.csv", yulesK)
# computeTextStatistics("data/hemingway/before_sun", "data/analysis_results/before_sun/yules_k.csv", yulesK)
# computeTextStatistics("data/token_lists/without_punctuation/with_stopwords", "data/analysis_results/reading_list/yules_k.csv", yulesK)

# computeTextStatistics("data/hemingway/sun", "data/analysis_results/sun/hapax_legomena_percentage.csv", hapax_legomena_percentage)
# computeTextStatistics("data/hemingway/before_sun", "data/analysis_results/before_sun/hapax_legomena_percentage.csv", hapax_legomena_percentage)
# computeTextStatistics("data/token_lists/without_punctuation/with_stopwords", "data/analysis_results/reading_list/hapax_legomena_percentage.csv", hapax_legomena_percentage)

# computeTextStatistics("data/hemingway/sun", "data/analysis_results/sun/average_sentence_length.csv", average_sentence_length)
# computeTextStatistics("data/hemingway/before_sun", "data/analysis_results/before_sun/average_sentence_length.csv", average_sentence_length)
# computeTextStatistics("data/clean_books", "data/analysis_results/reading_list/average_sentence_length.csv", average_sentence_length)
