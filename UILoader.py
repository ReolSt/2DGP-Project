from Engine.Singleton import Singleton
from Engine.Settings import Settings
from Engine.Scene import Scene
from Engine.GameObject import GameObject
from Engine.Text import Text
from Engine.EntitySprite import EntitySprite
from Engine.TerrainSprite import TerrainSprite

class UISlot:
    def __init__(self, slotName, slotType, gameObject):
        self.slotName = slotName
        self.slotType = slotType
        self.gameObject = gameObject

class UILoader(metaclass=Singleton):
    def __init__(self):
        self.uiFilePath = Settings().ui["UIFilePath"]

    def load(self, parent, fileName):
        uiFilePath = self.uiFilePath + fileName + ".txt"

        slots = {}

        with open(uiFilePath, "r") as file:
            for line in file.readlines():
                tokens = line.split()

                slotName, slotType = tokens[:2]

                gameObject = None

                if slotType == "Text":
                    slotName, slotType, x, y, xScale, yScale, spacing = tokens
                    gameObject = Text(parent, "", float(spacing))
                elif slotType == "Entity":
                    slotName, slotType, spriteName, x, y, xScale, yScale = tokens
                    gameObject = GameObject(parent)
                    gameObject.sprites.append(EntitySprite(gameObject, spriteName))
                elif slotType == "Terrain":
                    slotName, slotType, spriteName, x, y, xScale, yScale = tokens
                    gameObject = GameObject(parent)
                    gameObject.sprites.append(TerrainSprite(gameObject, spriteName))

                assert gameObject is not None, "[UILoader] load : Game object load error. ( {} )".format(line)

                x, y, xScale, yScale = float(x), float(y), float(xScale), float(yScale)

                gameObject.transform.translate(x, y)
                gameObject.transform.setLocalScale(xScale, yScale)
                slots[slotName] = UISlot(slotName, slotType, gameObject)

        return slots