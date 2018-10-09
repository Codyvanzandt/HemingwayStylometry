import distinct_words
import numpy.random

class TextSimulator(object):

    def __init__(self, frequencyTSVPath):
        self.frequencyTSVPath = frequencyTSVPath
        self._loadFrequencies()

    def _loadFrequencies(self):
        counts = distinct_words.makeCountDict(self.frequencyTSVPath)
        totalNumberTokens = sum( counts.values() )
        freqDict = { token : count / totalNumberTokens for token, count in counts.items() }
        self.tokens, self.frequencies = zip(*freqDict.items())

    def drawTokens(self, n=1):
        return numpy.random.choice(self.tokens, size=n, p=self.frequencies)

    def drawSentences(self, n=1):
        """
        Prefer drawTokens over drawSentences.
        Only use drawSentence if you need to maintain the original corpus's sentence length distribution.
        Because drawSentence tries to preserve the sentence length distribution by drawing
        until it hits a terminal punctuation token, it can be unboundedly slow.
        """
        return [ " ".join( self._drawSentence() ) for i in range(n) ]

    def _drawSentence(self):
        sentence = list()
        currentToken = str()
        terminalPunctuation = {".", "!", "?"}
        while currentToken not in terminalPunctuation:
            currentToken = self.drawTokens(n=None)
            sentence.append(currentToken)
        return sentence
