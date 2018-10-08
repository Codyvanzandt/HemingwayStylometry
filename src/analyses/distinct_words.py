import textblob
import collections
import corpus_statistics
import pandas

pandas.set_option("max_columns", None)
pandas.set_option("max_rows", None)


def makeFreqDict(filePath):
	d = dict()
	with open(filePath, "r") as f:
		for line in f:
			word, count = line.split("\t")
			d[word] = int(count.strip())
	return d

def getMostCommonFrequencies(inputDirectory, wordFilter, n):
	inputText = corpus_statistics.getAllText(inputDirectory)
	inputBlob = textblob.TextBlob(inputText)
	words = wordFilter(inputBlob)
	numberWords = len(words)
	counts = collections.Counter(words)
	mostCommon = dict(counts.most_common(n))
	return { word : count / numberWords for word, count in mostCommon.items() }

def getNonProperNouns(blob):
    nonProperNouns = {"NN", "NNS"}
    return [word.lower() for word, pos in blob.tags if pos in nonProperNouns and "'" not in word and word not in ["s","t"] ]

def getVerbs(blob):
    verbTags = {"VB", "VBD", "VBG", "VBN", "VBP", "VBZ"}
    return [word.lower() for word, pos in blob.tags if pos in verbTags and "'" not in word and word not in ["s","t"]]

def getAdjectives(blob):
    return [word.lower() for word, pos in blob.tags if pos.startswith("JJ") and "'" not in word and word not in ["s","t"]]

def getAdverbs(blob):
    return [word.lower() for word, pos in blob.tags if pos.startswith("RB") and "'" not in word and word not in ["s","t"]]

def getFunctionWords(blob):
    functionWords = {"CC", "DT", "EX", "IN", "MD", "PDT", "POS", "PRP", "RP", "TO", "UH", "WDT", "WP", "WP$", "WRB"}
    return [word.lower() for word, pos in blob.tags if pos in functionWords]

turgnevCommon = getMostCommonFrequencies("data/turgenev",getFunctionWords, None)
beforeCommon = getMostCommonFrequencies("data/hemingway/before_sun",getFunctionWords, None)
sunCommon = getMostCommonFrequencies("data/hemingway/sun",getFunctionWords, None)

works_1835_1869 = makeFreqDict("data/frequency_1835-1869")
early_works_total_words = sum(works_1835_1869.values())

works_1920_1922 = makeFreqDict("data/frequency_1920-1922")
late_works_total_words = sum(works_1920_1922.values())



# distinctiveness = list()
# for word, t_freq in turgnevCommon.items():
#     if word in works_1835_1869:
#         freq = works_1835_1869[word] / early_works_total_words
#         r = (word, t_freq / freq)
#         distinctiveness.append(r)
#
# h_distinctiveness = list()
# for word, h_freq in sunCommon.items():
#     if word in works_1920_1922:
#         freq = works_1920_1922[word] / late_works_total_words
#         r = (word, h_freq / freq)
#         h_distinctiveness.append(r)
#
# b_distinctiveness = list()
# for word, b_freq in beforeCommon.items():
#     if word in works_1920_1922:
#         freq = works_1920_1922[word] / late_works_total_words
#         r = (word, b_freq / freq)
#         b_distinctiveness.append(r)
#
#
# distinctiveness.sort( reverse=True, key=lambda x: x[1] )
# h_distinctiveness.sort( reverse=True, key=lambda x: x[1] )
# b_distinctiveness.sort( reverse=True, key=lambda x: x[1] )
#
# turgenev = distinctiveness[:50] + distinctiveness[-50:]
# before = b_distinctiveness[:50] + b_distinctiveness[-50:]
# sun = h_distinctiveness[:50] + h_distinctiveness[-50:]
#
# with open("data/distinct_function_words.csv", "w") as f:
#     f.write("Turgenev\tBefore\tSun\n")
#     for i, (p0, p1, p2) in enumerate(zip(turgenev, before, sun)):
#         f.write(f"{p0}\t{p1}\t{p2}\n")
