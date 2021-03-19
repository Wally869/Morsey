from typing import List

from Morse import * 
from SoundGenerator import SOUND_GENERATOR, SoundGenerator  

import numpy as np


def StringToSound(textInput: str, soundGenerator: SoundGenerator = SOUND_GENERATOR) -> np.array:
    morse = SentenceToMorse(textInput)
    allData = []
    for elem in morse:
        for idChar in range(len(elem)):
            if elem[idChar] == ".":
                allData.append(soundGenerator.GenerateDot())
            elif elem[idChar] == "-":
                allData.append(soundGenerator.GenerateDash())
            elif elem[idChar] == " ":
                allData.append(soundGenerator.GenerateSpace(1))
            elif elem[idChar] == "   ":
                allData.append(soundGenerator.GenerateSpace(3)) 
            else:  # word[idChar] == "     ":
                allData.append(soundGenerator.GenerateSpace(5)) 
    return np.concatenate(allData)

            

