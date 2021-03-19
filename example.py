

from main import *


if __name__ == "__main__":
    data = StringToSound("This is an example")
    SOUND_GENERATOR.PlaySound(data)
    SOUND_GENERATOR.SaveSoundToWav("media/example.wav", data)

