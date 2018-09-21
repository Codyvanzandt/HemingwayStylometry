from src.analyses import corpus_statistics, style_markers
from src import csv_utilities

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

import textblob
import os
import pandas
import collections

pandas.set_option("max_columns", None)

def getMostCommonWordFrequencies(directory,n):
    blob = textblob.TextBlob(corpus_statistics.getAllText(directory))
    words = [ word.lower() for word in blob.words ]
    numberWords = len(words)
    return { word: num / numberWords for word, num in collections.Counter(words).most_common(n)}

# sunTop50 = getMostCommonWordFrequencies("data/hemingway/sun", 50)
# beforeSunTop50 = getMostCommonWordFrequencies("data/hemingway/before_sun", 50)
# turgenevTop50 = getMostCommonWordFrequencies("data/turgenev",50)
#
# common = list( set.intersection( set(sunTop50.keys()), set(beforeSunTop50.keys()), set(turgenevTop50.keys()) ) )

def getFrequencyPerBlock(pathToBlock):
    blockText = " ".join(style_markers.readBlock(pathToBlock))
    blockBlob = textblob.TextBlob(blockText)
    blockWords = [ word.lower() for word in blockBlob.words ]
    numberWords = len(blockWords)
    wordCounter = collections.Counter(blockWords)
    return [ wordCounter[word] / numberWords for word in common ]

def getBlockPaths(pathToDirectory):
    return [ os.path.join(pathToDirectory, fileName) for fileName in csv_utilities.listCSVFiles(pathToDirectory) ]

def getFrequenciesForAllBlocks(pathToDirectory, blockType):
    return [getFrequencyPerBlock(blockPath) + [blockType] for blockPath in getBlockPaths(pathToDirectory)]

# turgenevFreqs = getFrequenciesForAllBlocks("data/block_size_5000/turgenev", "Turgenev's Works")
# sunFreqs = getFrequenciesForAllBlocks("data/block_size_5000/sun", "The Sun Also Rises")
# beforeFreqs = getFrequenciesForAllBlocks("data/block_size_5000/before_sun", "Hemingway's Prior Works")
#
# freqs = pandas.DataFrame(turgenevFreqs + sunFreqs + beforeFreqs, columns=list(range(len(common)))+["target"])
#
# X = StandardScaler().fit_transform( freqs.iloc[:,0:-1].values )
# Y = freqs.iloc[:,-1]
#
# pca = PCA(n_components=2)
# principalComponents = pca.fit_transform(X)
#
# principalComponentDF = pandas.DataFrame(data = principalComponents, columns = ['Principal Component 1', 'Principal Component 2',])
#
# labeledPCDF = pandas.concat([principalComponentDF, Y], axis = 1)
