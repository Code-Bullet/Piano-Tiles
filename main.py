import numpy as np
from PIL import ImageGrab
import cv2
from directKeys import click, queryMousePosition
import time

#
# click(1800, 10)
# time.sleep(1)

# gameCoords = [657, 232, 1262, 1039]
gameCoords = [656, 32, 1222, 1037]

smallerGameCoords = [657, 800, 1262, 802]
score = 0
previousLane = -1


def clickOnFirstBlock(screen):
    global gameCoords, score, previousLane
    for y_ in range(5, len(screen) - 5, 5):
        for i in range(4):
            if previousLane == i:
                continue
            w = gameCoords[2] - gameCoords[0]
            x = i * w / 4 + w / 8
            y = len(screen) - y_
            if screen[y][x] < 40:
                actualX = x + gameCoords[0]
                actualY = y + gameCoords[1]
                score += 1
                if score > 1000:
                    actualY += 10
                if score > 1250:
                    actualY += 10
                if score > 1450:
                    actualY += 10
                if score > 1600:
                    actualY += 20
                for k in range(1700, 2500):
                    if score > k:
                        actualY += 10
                    else:
                        break
                click(actualX, actualY)
                previousLane = i

                return
    # previousLane = -1


while True:
    mousePos = queryMousePosition()
    if mousePos.x < 0:
        break

while True:

    mousePos = queryMousePosition()

    if gameCoords[2] > mousePos.x > gameCoords[0]:
        startTime = time.time()
        screen = np.array(ImageGrab.grab(bbox=gameCoords))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        clickOnFirstBlock(screen)
        print("Frame took {} seconds. Up to frame no {}".format((time.time() - startTime), "FUCK YOU"))
    else:
        if mousePos.x < 0:
            score = 0
            while True:
                mousePos = queryMousePosition()
                if gameCoords[2] < mousePos.x:
                    break
