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

spell = SpellChecker()

response: dict[str, bool | str | int] = {
    "error": True,
    "string": "Unpopulated responce",
    "answer": 0,
}


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


def spell_check(spelling_text: str) -> dict[str, bool | str | int]:
    """
    Checks spelling in a multi-line text, identifies misspelled words,
    and suggests corrections.
    """

    if not isinstance(spelling_text, str):
        response["string"] = "Invalid Type - Text is not a string"
        return response

    if spelling_text == "":
        response["string"] = "Empty parameters - Text is not a string"
        return response
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
    response["error"] = False

    response["string"] = ", ".join(spelling_mistake_messages)
    if not spelling_mistake_messages:
        response["string"] = "There are no misspelled words in this text."
    response["answer"] = len(spelling_mistake_messages)
    return response
