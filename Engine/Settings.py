import configparser

from .Singleton import *

class Settings(metaclass=Singleton):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Settings, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        config = configparser.ConfigParser()
        config.read("Engine/Settings.ini")

        self.default = config['Default']
        self.sprite = config['Sprite']
        self.audio = config['Audio']