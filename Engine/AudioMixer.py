import os
import pico2d

if os.path.dirname(os.path.abspath(__file__)) == os.getcwd():
    from Singleton import *
    from Settings import *
else:
    from .Singleton import *
    from .Settings import *

class AudioMixer(metaclass=Singleton):
    def __init__(self):

        self.wavs = {}
        self.musics = {}

        audioFilePath = Settings().audio["AudioFilePath"]

        with open(Settings().audio["MusicFileListPath"], "r") as file:
            for line in file.readlines():
                tokens = line.split()
                if len(tokens) < 2:
                    continue

                name, fileName = tokens

                self.musics[name] = pico2d.load_music(audioFilePath + fileName)

        with open(Settings().audio["WavFileListPath"], "r") as file:
            for line in file.readlines():
                tokens = line.split()
                if len(tokens) < 2:
                    continue

                name, fileName = tokens

                self.wavs[name] = pico2d.load_wav(audioFilePath + fileName)

    def getVolumeWav(self, name):
        assert name in self.wavs, "Can't get wav volume : {}".format(name)

        return self.wavs[name].get_volume()

    def setVolumeWav(self, name, volume):
        assert name in self.wavs, "Can't set wav volume : {}".format(name)

        self.wavs[name].set_volume(volume)

    def playWav(self, name):
        assert name in self.wavs, "Can't play wav : {}".format(name)

        self.wavs[name].play()

    def getVolumeMusic(self, name):
        assert name in self.wavs, "Can't get music volume : {}".format(name)

        return self.musics[name].get_volume()

    def setVolumeMusic(self, name, volume):
        assert name in self.wavs, "Can't set music volume : {}".format(name)

        self.musics[name].set_volume(volume)

    def playMusic(self, name):
        assert name in self.musics, "Can't play music : {}".format(name)

        self.musics[name].play()

    def playMusicRepeat(self, name):
        assert name in self.musics, "Can't stop music : {}".format(name)

        self.musics[name].repeat_play()

    def stopMusic(self, name):
        assert name in self.musics, "Can't stop music : {}".format(name)

        self.musics[name].stop()

    def pauseMusic(self, name):
        assert name in self.musics, "Can't pause music : {}".format(name)

        self.musics[name].pause()

    def resumeMusic(self, name):
        assert name in self.musics, "Can't resume music : {}".format(name)

        self.musics[name].resume()

