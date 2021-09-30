import configparser

from Singleton import *

class Settings(Singleton):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("Settings.ini")

        self.default = config['Default']
        self.sprite = config['Sprite']