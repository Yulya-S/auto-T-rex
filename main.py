import pyautogui as pag
import matplotlib.pyplot as plt
import numpy as np


def image(name: str, y: int, img_number: int, width: int):
    pag.screenshot(f"{name}/img_{img_number}.png", (600 + 92, y, width, 1))
    img = plt.imread(f"{name}/img_{img_number}.png")
    img = np.array(img).mean(2)

    img[img < 0.8] = 1
    img[img != 1] = 0

    return 1 in img


img_number = 0
fast = 120
f = 0

while 1:
    if image("bottom_line", 394, img_number, fast):
        pag.press("space")
    elif image("middle_line", 359, img_number, fast):
        pag.press("space")

    img_number += 1
    f += 1
    if img_number >= 10:
        img_number = 0

    if f > 100 + 90 - fast:
        fast += 5
        if fast > 200:
            fast = 200
        f = 0
