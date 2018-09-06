import os
import sys
import collections
import itertools
import pprint
sys.path.append("/home/cody/hemingwayStylometry/src")
import csv_utilities


allFiles = csv_utilities.loadAllCSVFiles("data/token_lists/without_punctuation/without_stopwords")

wordList = itertools.chain.from_iterable(wordList for wordList in allFiles.values())

frequencies = collections.Counter(wordList)

pprint.pprint(frequencies.most_common(100))
