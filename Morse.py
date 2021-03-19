from typing import List

import json

ALLOWED_CHARACTERS = []

CHARACTERS_TO_MORSE = {}


with open('morse-code.json') as json_file: 
    CHARACTERS_TO_MORSE = json.load(json_file) 

for k, _ in CHARACTERS_TO_MORSE.items():
    ALLOWED_CHARACTERS.append(k)


def CharacterToMorse(char: str):
    morse = CHARACTERS_TO_MORSE[char]
    output = []
    for idSignal in range(len(morse)):
        output.append(morse[idSignal])
        if (idSignal != len(morse) - 1):
            output.append(" ")
    return output


def WordToMorse(word: str) -> List[str]:
    word = word.lower()
    output = []
    for idChar in range(len(word)):
        output += CharacterToMorse(word[idChar])
        #output.append(CHARACTERS_TO_MORSE[word[idChar]])
        if idChar != len(word) - 1:
            output.append("   ")
    return output

def SentenceToMorse(sentence: str) -> List[str]:
    splits = sentence.split(" ")
    converted = []
    for idWord in range(len(splits)):
        converted += WordToMorse(splits[idWord])
        if (idWord != len(splits) - 1):
            converted.append("       ")
    return converted