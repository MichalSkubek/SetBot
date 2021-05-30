from PIL import ImageGrab
from PIL import Image
from Classes.Card import Card
import time


class ScreenReader:

    @staticmethod
    def get_first_x_y(image: Image):
        x = 342
        y = 200
        for i in range(image.width):
            if image.getpixel((i, 50)) == (255, 255, 255):
                continue
            else:
                x += i
                break
        for i in range(image.height):
            if image.getpixel((30, i)) == (255, 255, 255):
                continue
            else:
                y += i
                break
        return x, y

    @staticmethod
    def get_number(image: Image):
        if image.getpixel((image.width/2, 16)) == (255, 255, 255):
            return 2
        else:
            if image.getpixel((42, 16)) == (255, 255, 255):
                return 1
            else:
                return 3

    @staticmethod
    def get_texture(image):
        if image.getpixel((image.width/2, 16)) == (255, 255, 255):
            if image.getpixel((66, 55)) == (255, 255, 255):
                # Check neighbour pixels for 100% accuracy
                w = int(image.width/2)
                for h in range(10, 20):
                    if image.getpixel((w, h)) != (255, 255, 255):
                        return 'shaded'
                return 'hollow'
            elif image.getpixel((66, 55))[2] in (1, 2, 128):
                return 'filled'
            else:
                return 'shaded'
        else:
            if image.getpixel((image.width/2, 55)) == (255, 255, 255):
                # Check neighbour pixels for 100% accuracy
                w = int(image.width/2)
                for h in range(50, 60):
                    if image.getpixel((w, h)) != (255, 255, 255):
                        return 'shaded'
                return 'hollow'
            elif image.getpixel((image.width/2, 55))[2] in (1, 2, 128):
                return 'filled'
            else:
                return 'shaded'

    @staticmethod
    def get_shape(image: Image):
        if image.getpixel((image.width / 2, 16)) == (255, 255, 255):
            if image.getpixel((61, 16)) == (255, 255, 255):
                return 'diamond'
            elif image.getpixel((48, 25)) == (255, 255, 255):
                return 'oval'
            else:
                return 'weird'
        else:
            if image.getpixel((image.width/2-4, 16)) == (255, 255, 255):
                return 'diamond'
            elif image.getpixel((71, 25)) == (255, 255, 255):
                return 'oval'
            else:
                return 'weird'

    @staticmethod
    def get_color(image: Image):
        if image.getpixel((image.width/2, 16)) == (255, 255, 255):
            if image.getpixel((66, 16))[0] in (128, 152):
                return 'violet'
            elif image.getpixel((66, 16))[0] in (0, 49):
                return 'green'
            else:
                return 'red'
        else:
            if image.getpixel((image.width/2, 16))[0] in (128, 152):
                return 'violet'
            elif image.getpixel((image.width/2, 16))[0] in (0, 49):
                return 'green'
            else:
                return 'red'

    @staticmethod
    def get_cards_from_screen():
        im = ImageGrab.grab(bbox=(342, 200, 725, 350))
        screen_x_1, screen_y_1 = ScreenReader().get_first_x_y(im)
        screen_x_2 = screen_x_1 + 177
        screen_y_2 = screen_y_1 + 106
        width = screen_x_2 - screen_x_1
        height = screen_y_2 - screen_y_1
        x_beetween = 13
        y_beetween = 13
        cards = list()
        for row in range(4):
            cont = True
            for column in range(3):
                x_1 = screen_x_1 + column * (width + x_beetween)
                y_1 = screen_y_1 + row * (height + y_beetween)
                x_2 = screen_x_2 + column * (width + x_beetween)
                y_2 = screen_y_2 + row * (height + y_beetween)
                if row == 4:
                    y_1 -= 1
                im = ImageGrab.grab(bbox=(x_1, y_1, x_2, y_2))
                im = im.convert('RGB')
                if im.getpixel((10, 0)) != (33, 33, 33):
                    cont = False
                    break
                cards.append(Card(
                    ScreenReader().get_color(im),
                    ScreenReader().get_shape(im),
                    ScreenReader().get_texture(im),
                    ScreenReader().get_number(im)
                ))
            if not cont:
                break

        return cards
