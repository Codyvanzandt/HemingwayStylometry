import distinct_words
import corpus_statistics
import textblob

# works_1835_1869 = distinct_words.makeFreqDict("data/frequency_1835-1869")
# early_works_total_words = sum(works_1835_1869.values())
#
# works_1920_1922 = distinct_words.makeFreqDict("data/frequency_1920-1922")

coordinators = {"for", "and", "nor", "but", "or", "yet", "so"}
subordinators = {"after", "although", "as", "though", "because", "before", "even",
"if", "lest", "once", "since", "than", "that", "though", "unless", "until", "when",
"whenever", "where", "wherever", "while"}
to_be = { "is", "are", "was", "were", "am", "been", "be", "being"}

text = textblob.TextBlob( corpus_statistics.getAllText("data/turgenev") )
total_tokens = len(text.tokens)

internal_punctuation = { ",", ":", ";", "-"}
terminal_punctuation = {".", "!", "?"}

occurences = [ token for token in text.tokens if token.endswith("ing") ]

print(f"Turgenev Hyphenated Compounds {len(occurences) / total_tokens }")

# all_tokens = 0
# specific_tokens = 0
# for word, count in works_1920_1922.items():
#     if word in terminating_punctuation:
#         specific_tokens += count
#     all_tokens += count
#
# print(f"1920-1922 Terminating Punctuation: {specific_tokens / all_tokens}")
