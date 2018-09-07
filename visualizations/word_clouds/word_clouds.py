from wordcloud import WordCloud

import collections
import itertools
import matplotlib.pyplot as plt
import csv_utilities

def getWordFrequencies(pathToDirectory):
    allFiles = csv_utilities.loadAllCSVFiles(pathToDirectory)
    wordList = itertools.chain.from_iterable(wordList for wordList in allFiles.values())
    frequencies = collections.Counter(wordList)
    return frequencies

def makeWordCloud(frequencies,n):
    most_common = dict(frequencies.most_common(n))

    wc = WordCloud(background_color="white", max_words=n, width=1000, height=500)
    wc.generate_from_frequencies(most_common)

    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

# nounFrequencies = getWordFrequencies("data/token_lists/parts_of_speech/simple_nouns")
# properNounFrequencies = getWordFrequencies("data/token_lists/parts_of_speech/proper_nouns")
# verbFrequencies = getWordFrequencies("data/token_lists/parts_of_speech/verbs")
# adjectiveFrequencies = getWordFrequencies("data/token_lists/parts_of_speech/adjectives")
# adverbFrequencies = getWordFrequencies("data/token_lists/parts_of_speech/adverbs")
#
# makeWordCloud(adverbFrequencies,200)
