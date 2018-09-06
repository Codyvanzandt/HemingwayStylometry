# Hemingway Stylometry

## Short Introduction
A public repository to house my research on Hemingway's Paris reading list.

This repository contains everything - code files, notes, articles, visualizations, etc. - from every step in my research process.

Big thanks to Princeton's [Mapping Expatriate Paris project](https://github.com/Princeton-CDH/mapping-expatriate-paris) for opening up their data to the public! The file /data/hemingway.tei.xml comes from their repository.

All texts included in data/ are, to the best of my knowledge, in US public domain. I have sourced them from a variety of online locations. The sources are noted in /data/books_before_sun.csv. If you would like to use these texts, please take care to cite the original electronic versions.

## What's in /data?

### /data files
- **hemingway.tei.xml**
  - XML markups of Hemingway's library cards from the Shakespeare and Company lending library. Source: the Mapping Expatriate Paris project.
- **hemingway_borrowing.csv**
  - A .csv file of `DateBorrowed,DateReturned,Title` with a prepended index column. This .csv was created from **hemingway.tei.xml**
- **books_before_sun.csv**
  - A .csv file of `Title,Author,Included,Source` for all the books Hemingway checked out from the begining of the dataset to
  when he finished *The Sun Also Rises*. `
    - `Included` is a boolean: whether or not this work was included in the analysis. Some texts are excluded because proper electronic versions could not be freely obtained. Other texts are excluded because they were written by Hemingway himself.
    
### data/books
**data/books** contains plain text versions of every book in **books_before_sun.csv** for which `Include` is true.

### data/clean_books
**data/clean_books** contains the same texts as data/books, except that these texts have been cleaned on a "best effort" basis. Page numbers, chapter headings, digitizer marks, and other problematic strings have been removed. You can see exactly what was removed by inspecting **src/cleaning.py**

### data/token_lists
**data/token_lists** contain various kinds of token lists (as .csv files with one word per line) for every book in **data/clean_books** For every book, you can find token lists 1. with or without stopwords and 2. with or without punctuation. You can also find a token list of just punctuation. Directory paths indicate the contents.
