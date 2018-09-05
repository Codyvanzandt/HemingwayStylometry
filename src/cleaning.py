import re
from unidecode import unidecode

# de-unicoding
re.sub(r'[^\x00-\x7F]+','', text)

# removing urls
re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)

# Removing chapter, page, and paragraph markings
("along_the_road.txt", r"^\d+\n"),
("buddenbrooks.txt", r"^\d+\n"),
("far_away_and_long_ago.txt", r"^CHAPTER\s*[I|V|X|L|C|D]+")
("flurried_years.txt", r"\d*\s*The\s*Flurried\s*Years\s*\d*")
("house_of_gentle_folks.txt",r"^Chapter\s*[I|V|X|L|C|D]+" )
("knock_knock_knock.txt", r"^[I|V|X|L|C|D]+\n")
("lear_of_the_steppes.txt", r"^[I|V|X|L|C|D]+\n")
("more_tales_of_the_uneasy.txt", r"\d*\s*[A-Za-z]+\s*\d*")
("on_the_eve.txt", r"^[I|V|X|L|C|D]+\n")
("outcast_of_the_islands.txt", r"CHAPTER\s*[A-Z]+")
("parody_outline_of_history.txt", r"(Chapter|CHAPTER|chapter)\s*[a-zA-z]+")
("parody_outline_of_history.txt", r"^[I|V|X|L|C|D]+\n")
("parody_outline_of_history.txt", r"^(Scene|SCENE|Scene)\s*.*$")
("problems_of_philosophy.txt", r"CHAPTER\s*[I|V|X|L|C|D]+\.")
("sailing_around_the_world.txt", r"^CHAPTER\s*[I|V|X|L|C|D]+")
("sea_and_the_jungle.txt", r"^[I|V|X|L|C|D]+\n")
("sea_and_the_jungle.txt", r"^\s*(\*|\s)+\s*$")
("sentimental_education.txt",r"^CHAPTER\s*[I|V|X|L|C|D]+\.?")
("sportsmans_sketches_2.txt", r"^[I|V|X|L|C|D]+\.?")
("steeplejack.txt", r"^[0-9]*\s*(STEEPLEJACK|Steeplejack|steeplejack)\s*[0-9]*$")
("steeplejack.txt", r"^[I|V|X|L|C|D]+")
("steeplejack.txt", r"^[0-9|i|I|V|X|L|C|D|\s]*\s*(STEEPLEJACK|Steeplejack|steeplejack)+\s*[0-9|i|I|V|X|L|C|D|\s]*$")


# Removing repeated title
 ("along_the_road.txt", r"ALONG\s+THE\s+ROAD"),
 ("buddenbrooks.txt", r"BUDDENBROOKS"),

# Accessed at
("collected_poems.txt", r"Last updated.*$")

# Digitizer markup
("more_tales_of_the_uneasy.txt", r"Digitized by")
("more_tales_of_the_uneasy.txt", r"Google")

# Illustration tags
("sailing_around_the_world.txt", r"\[Illustration:")
("sailing_around_the_world.txt", r"\]$")
