import pico2d

from .Singleton import *
from .Settings import *

class AudioMixer(metaclass=Singleton):
    def __init__(self):

        self.wavs = {}

        audioFilePath = Settings().audio["AudioFilePath"]

        with open(Settings().audio["AudioFileListPath"], "r") as file:
            for line in file.readlines():
                tokens = line.split()
                if len(tokens) < 2:
                    continue

                name, fileName = tokens

                self.wavs[name] = pico2d.load_wav(audioFilePath + fileName)

    def play(self, name):
        assert name in self.wavs, "Can't play wav : {}".format(name)

        self.wavs[name].play()

