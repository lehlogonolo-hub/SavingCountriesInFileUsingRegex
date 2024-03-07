# Author: Aphane Jimmy

from data import countries_and_capitals, countries, capitals, countries_capitals_dictionary
import project
import re


def main():
    project.write_countries_capitals_to_file("data.txt")
    project.save_capitals()


if __name__ == "__main__":
    main()
