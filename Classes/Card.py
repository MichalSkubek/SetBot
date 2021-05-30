from .Enums.Color import Color
from .Enums.Shape import Shape
from .Enums.Texture import Texture
from .Enums.Number import Number


class Card:
    def __init__(self, color, shape, texture, number):
        # Colo(u)r
        self.color = Color(color)
        # Shape
        self.shape = Shape(shape)
        # Texture
        self.texture = Texture(texture)
        # Number
        self.number = Number(number)

    def __str__(self):
        return f"{self.color.value}, {self.shape.value}, {self.texture.value}, {self.number.value}\n"

    def __eq__(self, other):
        return self.color == other.color and self.shape == other.shape \
            and self.texture == other.texture and self.number == other.number

    def match_card(self, card):
        color = self.__match_color(card.color)
        shape = self.__match_shape(card.shape)
        texture = self.__match_texture(card.texture)
        number = self.__match_number(card.number)

        return Card(color, shape, texture, number)

    def __match_color(self, color):
        atr_set = set(Color)
        atr_set.discard(self.color)
        atr_set.discard(color)
        if len(atr_set) == 1:
            return atr_set.pop().value
        else:
            return self.color.value

    def __match_shape(self, shape):
        atr_set = set(Shape)
        atr_set.discard(self.shape)
        atr_set.discard(shape)
        if len(atr_set) == 1:
            return atr_set.pop().value
        else:
            return self.shape.value

    def __match_texture(self, texture):
        atr_set = set(Texture)
        atr_set.discard(self.texture)
        atr_set.discard(texture)
        if len(atr_set) == 1:
            return atr_set.pop().value
        else:
            return self.texture.value

    def __match_number(self, number):
        atr_set = set(Number)
        atr_set.discard(self.number)
        atr_set.discard(number)
        if len(atr_set) == 1:
            return atr_set.pop().value
        else:
            return self.number.value
