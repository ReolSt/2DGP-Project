import pico2d
from Transform import *
from GameObject import *

SPRITE_PATH = "resources/image/sprite/"

def get_sprites(sprite_type):
    sprite_image = pico2d.load_image(SPRITE_PATH + sprite_type + "Sprites.png")

    sprite_indices = {}
    with open(SPRITE_PATH + sprite_type + "SpriteIndex.txt", "r") as sprite_index_file:
        for line in sprite_index_file.readlines():
            tokens = line.split()
            if len(tokens) < 4:
                continue

            name, *positions = tokens
            start_x, start_y, end_x, end_y = map(int, positions)
            x = start_x
            y = start_y
            width = end_x - start_x + 1
            height = end_y - start_y + 1

            left = start_x
            bottom = sprite_image.h - end_y - 1

            sprite_indices[name] = {
                'x' : x,
                'y' : y,
                'width' : width,
                'height' : height,
                'left' : left,
                'bottom': bottom
            }

    return (sprite_image, sprite_indices)

def draw_sprite(sprite_image, sprite_index, x, y, scale):
    sprite_x = sprite_index['x']
    sprite_y = sprite_index['y']
    width = sprite_index['width']
    height = sprite_index['height']

    left = sprite_index['left']
    bottom = sprite_index['bottom']

    sprite_image.clip_draw(
        left, bottom, width, height, x, y, width * scale[0], height * scale[1])


class SpriteMap:
    def __init__(self, group):
        self.image = pico2d.load_image(SPRITE_PATH + group + "Sprites.png")
        self.indices = {}

        with open(SPRITE_PATH + group + "SpriteIndex.txt", "r") as index_file:
            for line in index_file.readlines():
                tokens = line.split()
                if len(tokens) < 4:
                    continue

                name, *positions = tokens
                startX, startY, endX, endY = map(int, positions)
                x = startX
                y = startX
                width = endX - startX + 1
                height = endY - startY + 1

                left = startX
                bottom = self.image.h - endY - 1

                self.indices[name] = {
                    'x': x,
                    'y': y,
                    'width': width,
                    'height': height,
                    'left': left,
                    'bottom': bottom
                }

    def getIndex(self, name):
        return self.indices[name]


class Sprite:
    def __init__(self, spriteMap, spriteName, parent):
        self.spriteMap = spriteMap
        self.spriteName = spriteName
        self.spriteIndex = self.spriteMap.indices[self.spriteName]

        self.width = self.spriteIndex['width']
        self.height = self.spriteIndex['height']
        self.left = self.spriteIndex['left']
        self.bottom = self.spriteIndex['bottom']

        if type(parent) is GameObject:
            parent = parent.transform

        self.transform = Transform(parent)

    def render(self):

        spriteIndex = self.spriteMap.indices[self.spriteName]

        x, y = self.transform.position()
        rotation = self.transform.rotation()
        scale = self.transform.scale()
        flip = self.transform.flip()

        flipString = '' + ('h' if flip[0] else '') + ('v' if flip[1] else '')

        self.spriteMap.image.clip_composite_draw(
            self.left, self.bottom, self.width, self.height, rotation, flipString, x, y,
            self.width * scale[0], self.height * scale[1])