

import numpy as np 
import soundcard as sc

DFLT_SPEAKER = sc.default_speaker()



class SoundGenerator(object):
    def __init__(self, frequency: int, dotDurationMilliseconds: int, sampleRate: int = 4000):
        self.mFrequency = frequency
        self.mDotDuration = dotDurationMilliseconds # in milliseconds
        self.mSampleRate = sampleRate
    def GenerateSound(self, duration: float, amplitude: float = 1.0) -> np.array:
        return amplitude * np.sin(2 * np.pi * self.mFrequency * np.arange(duration * self.mSampleRate) / self.mSampleRate)
    def GenerateDot(self) -> np.array:
        return self.GenerateSound(self.mDotDuration / 1000)
    def GenerateDash(self) -> np.array:
        return self.GenerateSound(self.mDotDuration * 3 / 1000)
    def GenerateSpace(self, lengthSpace: int) -> np.array:
        return self.GenerateSound(self.mDotDuration * lengthSpace / 1000, 0.0)
    def PlaySound(self, data: np.array) -> None:
        DFLT_SPEAKER.play(data, self.mSampleRate)
    def SaveSoundToWav(self, fileName: str, data: np.array) -> None:
        from scipy.io.wavfile import write
        write(fileName, self.mSampleRate, data)


SOUND_GENERATOR = SoundGenerator(440, 50, 4000)


def PlaySound(array: np.array, sampleRate: int):
    DFLT_SPEAKER.play(array, sampleRate)
