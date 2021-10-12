import time
import numpy

import pico2d

from Engine.Settings import *
from Engine.RenderingContext import *

settings = Settings()
renderingContext = RenderingContext(
    int(settings.default["WindowWidth"]), int(settings.default["WindowHeight"]))

from World1_1Scene import *

scene = World1_1Scene("World 1-1")
scene.debug = True

running = True
oldTime = time.time()
while running:
    currentTime = time.time()
    deltaTime = currentTime - oldTime

    pico2d.clear_canvas()

    scene.update(deltaTime * 1000)
    scene.render()

    pico2d.update_canvas()

    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_QUIT:
            running = False
            break
        else:
            scene.root.captureEvent(event)

    finishedTime = time.time()
    elapsedTime = finishedTime - currentTime

    pico2d.delay(max(0.0, 1 / int(settings.default['TargetFPS']) - elapsedTime))

    oldTime = currentTime

pico2d.close_canvas()