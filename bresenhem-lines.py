import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import imshow
from PIL import Image


def draw_line(img, x0 : int, y0 : int, x1 : int, y1 : int, color : tuple) -> None:
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        img.putpixel((x0, y0), color)
        if x0 == x1 and y0 == y1:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy



x0, y0 = map(int, input("(x0, y0): ").split())
x1, y1 = map(int, input("(x1, y1): ").split())

img = Image.new('RGB', (1000, 900), 'white')

draw_line(img, x0, y0, x1, y1, (255, 0, 0))

imshow(np.asarray(img))

plt.show()

img.save('line.jpg')