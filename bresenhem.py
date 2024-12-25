import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def draw_circle_pixels(img, xc : int, yc : int, x : int, y : int, color : tuple) -> None:
    img.putpixel((xc + x, yc + y), color)
    img.putpixel((xc - x, yc + y), color)
    img.putpixel((xc + x, yc - y), color)
    img.putpixel((xc - x, yc - y), color)
    img.putpixel((xc + y, yc + x), color)
    img.putpixel((xc - y, yc + x), color)
    img.putpixel((xc + y, yc - x), color)
    img.putpixel((xc - y, yc - x), color)


def bresenham_circle_algo(img, xc : int, yc : int, r : int, color : tuple) -> None:
    x = 0
    y = r
    d = 3 - 2 * r
    draw_circle_pixels(img, xc, yc, x, y, color)

    while y >= x:
        x += 1

        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6

        draw_circle_pixels(img, xc, yc, x, y, color)


rad = int(input())

image_size = 2 * rad + 20

xc, yc = image_size // 2, image_size // 2

img = Image.new('RGB', (image_size, image_size), 'white')

bresenham_circle_algo(img, xc, yc, rad, (255, 0, 0))

plt.imshow(np.asarray(img))
plt.show()

img.save('circle.jpg')