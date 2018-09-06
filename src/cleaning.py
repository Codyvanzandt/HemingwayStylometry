import re
import itertools
import logging

# Removing chapter, page, and paragraph markings
chapter_and_page = [("along_the_road.txt", r"^\d+"),
                    ("buddenbrooks.txt", r"^\d+"),
                    ("buddenbrooks.txt", "^CHAPTER\s*[I|V|X|L|C|D]+"),
                    ("far_away_and_long_ago.txt",
                     r"^CHAPTER\s*[I|V|X|L|C|D]+"),
                    ("flurried_years.txt", r"\d*\s*The\s*Flurried\s*Years\s*\d*"),
                    ("flurried_years.txt", r"\s*\*+\s*"),
                    ("house_of_gentle_folks.txt",
                     r"^Chapter\s*[I|V|X|L|C|D]+"),
                    ("knock_knock_knock.txt", r"^[I|V|X|L|C|D]+\n"),
                    ("lear_of_the_steppes.txt", r"^[I|V|X|L|C|D]+\n"),
                    ("more_tales_of_the_uneasy.txt", r"^\d+\s+[A-Z|\s]+$"),
                    ("more_tales_of_the_uneasy.txt", r"^[A-Z|\s]+\d+\s+$"),
                    ("more_tales_of_the_uneasy.txt", r"TALES OF T.*$"),
                    ("on_the_eve.txt", r"^[I|V|X|L|C|D]+\n"),
                    ("outcast_of_the_islands.txt", r"CHAPTER\s*[A-Z]+"),
                    ("parody_outline_of_history.txt",
                     r"(?:Chapter|CHAPTER|chapter)+\s[a-zA-z]+"),
                    ("parody_outline_of_history.txt", r"^[I|V|X|L|C|D]+\n"),
                    ("parody_outline_of_history.txt",
                     r"^\s*(?:Scene|SCENE|Scene)\s*.*"),
                    ("problems_of_philosophy.txt",
                     r"CHAPTER\s*[I|V|X|L|C|D]+\."),
                    ("sailing_around_the_world.txt",
                     r"^CHAPTER\s*[I|V|X|L|C|D]+"),
                    ("sea_and_the_jungle.txt", r"^[I|V|X|L|C|D]+\n"),
                    ("sea_and_the_jungle.txt", r"\s*\*+\s*"),
                    ("sentimental_education.txt",
                     r"^CHAPTER\s*[I|V|X|L|C|D]+\.?"),
                    ("sportsmans_sketches_2.txt", r"^[I|V|X|L|C|D]+\.?[A-Z]+?$"),
                    ("steeplejack.txt",
                     r"^[0-9]*\s*(?:STEEPLEJACK|Steeplejack|steeplejack)\s*[0-9]*$"),
                    ("steeplejack.txt", r"^[I|V|X|L|C|D]+$"),
                    ("steeplejack.txt",
                     r"^[0-9|i|I|V|X|L|C|D|\s]*\s*(?:STEEPLEJACK|Steeplejack|steeplejack)+\s*[0-9|i|I|V|X|L|C|D|\s]*$"),
                     ("steeplejack.txt", r"^\d+.*$"),
                     ("steeplejack.txt", r".*\d+$"),
                    ("strait_is_the_gate.txt",
                     r"(?:Chapter|CHAPTER|chapter)\s*[a-zA-z]+"),
                    ("strait_is_the_gate.txt", r"^\d+$"),
                    ("strait_is_the_gate.txt", r"^[I|V|X|L|C|D]+$"),
                    ("strait_is_the_gate.txt", r"^[i|v|x|l|c|d]+$"),
                    ("the_charterhouse_of_parma.txt", r"CHAPTER\s*[A-Z]+"),
                    ("the_charterhouse_of_parma.txt", r"VOLUME\s*[I|II]"),
                    ("the_crime_at_vanderlyndens.txt", r"^THE\s*CRI.*$"),
                    ("the_crime_at_vanderlyndens.txt", r"^AT\s*VA.*$"),
                    ("the_crime_at_vanderlyndens.txt", r"^\d+$"),
                    ("the_egoists.txt", r"^CHAPTER\s*[I|V|X|L|C|D]+"),
                    ("thus_spoke_zarathustra.txt", r"^\d+\."),
                    ("thus_spoke_zarathustra.txt", r"^[I|V|X|L|C|D]+\."),
                    ("travel_diary_of_a_philosopher.txt", r"^\s*\d+\s*"),
                    ("travel_diary_of_a_philosopher.txt", r"\s*\d+\s*$"),
                    ("travel_diary_of_a_philosopher.txt", r"^CHAP\.\s*."),
                    ("two_friends.txt", r"^\d+"),
                    ("two_friends.txt", r"^THE\s+TW.*$")
                    ]

# Removing repeated title
repeated_title = [("along_the_road.txt", r"ALONG\s+THE\s+ROAD"),
                  ("buddenbrooks.txt", r"BUDDENBROOKS"),
                  ("collected_poems.txt", r"Collected Poems, by William Butler Yeats")]

# Accessed at
accessed_at = [("collected_poems.txt", r"Last updated.*$")]

# Digitizer markup
digitizer = [("more_tales_of_the_uneasy.txt", r"Digitized by"),
             ("more_tales_of_the_uneasy.txt", r"Google")
             ]


# Illustration tags
illustrations = [("sailing_around_the_world.txt", r"\[Illustration:"),
                 ("sailing_around_the_world.txt", r"\]$")
                 ]


def cleanUpTexts():
    groupedByTitle = groupByTitle()
    for title, group in groupedByTitle:
        with open(f"data/books/{title}", "r") as textFile:
            text = textFile.read()
            text = makeGeneralChanges(text)
            for _, pattern in group:
                logging.info(f"Removing regex {pattern} from {title}")
                text = re.sub(pattern, "", text, flags=re.MULTILINE)
            with open(f"data/clean_books/{title}", "w") as cleanFile:
                logging.info(f"Writing {title} to data/clean_books")
                cleanFile.write(text)

def groupByTitle():
    allChanges = chapter_and_page + repeated_title + accessed_at + digitizer +illustrations
    return itertools.groupby(sorted(allChanges), key=lambda x: x[0])

def makeGeneralChanges(text):
    # remove unicode
    text = re.sub(r'[^\x00-\x7F]+', ' ', text, flags=re.MULTILINE)
    # remove urls
    text = re.sub(r'https?:\/\/.*', '', text, flags=re.MULTILINE)
    return text
