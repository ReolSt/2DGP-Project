import time

import pico2d

from Engine.Settings import *
from Engine.RenderingContext import *

settings = Settings()
renderingContext = RenderingContext(
    int(settings.default["WindowWidth"]), int(settings.default["WindowHeight"]))

from GamePlayScene import *

def main():
    scene = GamePlayScene()
    scene.loadWorld(1, 1)

    scene.debug = True

    running = True
    oldTime = time.time()
    while running:
        currentTime = time.time()
        deltaTime = currentTime - oldTime

        pico2d.clear_canvas()

        GameState().update(deltaTime * 1000)

        scene.update(deltaTime * 1000)
        scene.render()

        pico2d.update_canvas()

        events = pico2d.get_events()
        for event in events:
            if event.type == pico2d.SDL_QUIT:
                running = False
                break

            if event.type == pico2d.SDL_KEYDOWN:
                if event.key == pico2d.SDLK_F1:
                    scene.debug = not scene.debug

            scene.root.captureEvent(event)

        finishedTime = time.time()
        elapsedTime = finishedTime - currentTime

        delayTime = 1 / int(settings.default['TargetFPS']) - elapsedTime

        if delayTime > 0.0:
            pico2d.delay(delayTime)

        oldTime = currentTime

    pico2d.close_canvas()

if __name__ == "__main__":
    main()