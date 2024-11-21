from spellchecker import SpellChecker
import re

def line_stripper(line_text: str) -> list:
    cleaned_string = re.sub("[^A-Za-z\ ]","", line_text)
    return cleaned_string.split(" ")


def spell_check(spelling_text: str) -> tuple[int, list]:
    " -1 means not string, -2 means string is empty"
    if not isinstance(spelling_text, str):
        return -1, []
    if spelling_text == "":
        return -2, []

    spell = SpellChecker()
    
    spelling_mistake_by_line = spelling_text.split("\n")
    spelling_mistake_messages = []

    for i in range(0, len(spelling_mistake_by_line)):
        # find those words that may be misspelled
        misspelled = spell.unknown(line_stripper(spelling_mistake_by_line[i]))
        for word in misspelled:
            message_text = f"spelling mistake {word} on line {i} did you mean {spell.correction(word)}"
            spelling_mistake_messages.append(message_text)
    
    return len(spelling_mistake_messages), spelling_mistake_messages
