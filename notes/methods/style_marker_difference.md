# Experiment

0. Add In Our Time to Hemingway's (DONE)

1. Break up the texts into equal sized blocks (DONE)

2. Compute average and standard deviation of each marker. (DONE)
- Token Length (DONE)
- Distinct Word Length (DONE)
- Sentence Length (DONE)

3. Conduct a series of one-way ANOVA tests to investigate differences between corpora. (DONE)

4. Compute Frequency by Block (DONE)

5. Feature reduce the block data using PCA (DONE)

6. Plot the frequency data (DONE)

7. Repeat experiment for POS frequencies (DONE)

8. Read and annotate A Study in the Nature of Literary Influence

# Results

## Token Length

### Average and Standard Deviation

Before Sun (4.060540387749277, 0.15427649692398712)
Turgenev (4.269856752941347, 0.1574756594366673)
Sun (3.9038210466988628, 0.10870749649244611)

### ANOVA Results

Before Sun and Turgnev differ: p-value < 0.001
Turgenev and Sun differ: p-value < 0.000001
Before Sun and Sun differ: p-value 0.013


## Distinct Word Length

### Average, Standard Deviation
Before Sun (5.534873150141191, 0.18256183345987548)
Turgenev (6.0556321735127785, 0.220413197319947)
Sun (5.54148121632004, 0.12792135448519107)

### ANOVA Results
Before Sun and Turgnev differ: p-value < 0.000001
Turgenev and Sun differ: p-value < 0.0000001
Before Sun and Sun do not differ: p-value 0.923


## Sentence Length

### Average, Standard Deviation
Before Sun (12.475445023865714, 6.371874687445602)
Turgenev (15.734698853213878, 3.931691461944722)
Sun (8.867200876930163, 1.437952393213336)

### ANOVA Results
Before Sun and Turgnev differ: p-value 0.046
Turgenev and Sun differ: p-value < 0.0000001
Before Sun and Sun do not differ: p-value 0.061

## 50 Most Common Words

### Intersection of 50 most common words
['was', 'i', 'her', 'and', 'you', 'said', 'not', 'a', 'on', 'have', 'is', 'out', 'in', 'all', 'from', 'my', 'up', 'what', 'he', 'his', 'for', 'had', 'me', 'of', 'him', 'she', 'it', 'at', 'the', 'to', 'were', 'there', 'with', 'that', 'one']

### Average difference in frequency
Turgenev and Before Sun: 0.0036
Turgenev and Sun: 0.0037
Before Sun and Sun: 0.0022
