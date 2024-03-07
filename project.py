# Author: Aphane Jimmy

import re
from data import countries_and_capitals, countries, capitals, countries_capitals_dictionary


def write_countries_capitals_to_file(filename):
    while True:
        if not re.match(r"^[a-zA-Z0-9]{1,8}\.txt$", filename):
            filename = input("Enter a filename: ")
        else:
            break

    try:
        if len(filename) >= 1 or len(filename) <= 8:
            with open("data.txt", "w") as file:
                for country, capital in countries_capitals_dictionary.items():
                    file.write(f"The capital city of {country} is {capital}.\n")
                file.close()
    except Exception as e:
        print(f"Invalid filename: {e}\nFilename format must be of length 1-8 characters")


def save_capitals():
    patterns = {
        "vowel_vowel_vowel.txt": re.compile(r"[aeiouAEIOU]{3}"),
        "cons_cons_cons.txt": re.compile(r"[^aeiouAEIOU]{3}"),
        "i_before_e.txt": re.compile(r"i.*e"),
        "a_a.txt": re.compile(r"^[aA][\w\s]*[aA]$"),
        "end_with_vowel.txt": re.compile(r"[aeiouAEIOU]$"),
        "weird.txt": re.compile(r"[\' x ]"),
        "not_start.txt": re.compile(r"[^a-eL-Ps]")
    }

    for filename, pattern in patterns.items():
        with open(filename, 'w') as file:
            for country, capital in countries_capitals_dictionary.items():
                if re.match(pattern, capital):
                    file.write(capital + '\n')
            file.close()
