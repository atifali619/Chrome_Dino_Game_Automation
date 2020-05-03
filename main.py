import pyautogui
from PIL import Image, ImageGrab
import time


def hit(key):
    pyautogui.keyDown(key)


def isCollide(data):
    for i in range(215, 235):
        for j in range(275, 370):
            if data[i, j] < 100:
                hit("down")
                return True

    for i in range(220, 240):
        for j in range(370, 430):
            if data[i, j] < 100:
                hit("up")
                return True
    return False


if __name__ == "__main__":
    print("Game will start in 3 2 1.....")
    time.sleep(3)
    hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)


        # To check image co-ordinates

        # For Cactus
        # for i in range(220, 240):
        #     for j in range(370, 430):
        #         data[i, j] = 0
        #

        # For Bird
        # for i in range(215, 235):
        #     for j in range(275, 370):
        #         data[i, j] = 171
        #
        # image.show()
        # break
