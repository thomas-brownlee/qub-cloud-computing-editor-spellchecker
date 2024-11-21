"""
spell check
=================

This module provides functions to clean text lines and perform spell checking. 
It can identify misspelled words and suggest corrections for multi-line input.

Dependencies:
    - ``re``: For regular expression operations to clean text.
    - ``spellchecker``: For performing spell checking.

Functions:
    - :func:`line_stripper`
    - :func:`spell_check`
"""

import re

from spellchecker import SpellChecker


def line_stripper(line_text: str) -> list:
    """
    Strips non-alphabetic characters from a line of text and splits it into words.

    :param line_text: The text to process.
    :type line_text: str
    :return: A list of words from the cleaned text.
    :rtype: list

    :Example:

    >>> line_stripper("Hello, world!123")
    ['Hello', 'world']
    """
    string_with_spaces = line_text.replace("_", " ")
    cleaned_string = re.sub("[^A-Za-z ]", "", string_with_spaces)
    return cleaned_string.split(" ")


def spell_check(spelling_text: str) -> tuple[int, list]:
    """
    Checks spelling in a multi-line text, identifies misspelled words,
    and suggests corrections.

    :param spelling_text: A multi-line string containing the text to check.
    :type spelling_text: str
    :return:
        - An integer representing the number of misspelled words, or an error code:
            - ``-1``: Input is not a string.
            - ``-2``: Input string is empty.
        - A list of messages describing each misspelling and suggesting corrections.
    :rtype: tuple[int, list]

    :Example:

    >>> spell_check("Ths is a tst.\nHelo wrld!")
    (3, ['spelling mistake Ths on line 0 did you mean This',
         'spelling mistake tst on line 0 did you mean test',
         'spelling mistake Helo on line 1 did you mean Hello'])

    :Notes:
        - Each misspelled word is reported with the line number where it was found.
        - Suggestions are based on the closest match determined by the ``SpellChecker`` library.
    """
    if not isinstance(spelling_text, str):
        return -1, []
    if spelling_text == "":
        return -2, []

    spell = SpellChecker()

    spelling_mistake_by_line = spelling_text.split("\n")
    spelling_mistake_messages = []

    for i, line_message in enumerate(spelling_mistake_by_line):
        # Find words that may be misspelled
        misspelled = spell.unknown(line_stripper(line_message))
        for word in misspelled:
            message_text = (
                f"spelling mistake {word} on line "
                f"{i} did you mean {spell.correction(word)}"
            )
            spelling_mistake_messages.append(message_text)

    return len(spelling_mistake_messages), spelling_mistake_messages
