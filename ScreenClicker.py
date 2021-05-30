from random import randint, uniform
from pyautogui import click
from time import sleep


class ScreenClicker:
    def __init__(self, random=True, max_offset=10, col_first=442, col_diff=189, row_first=257, row_diff=118, cards_in_row=3):
        self.random = random
        self.max_offset = max_offset
        self.col_first = col_first
        self.col_diff = col_diff
        self.row_first = row_first
        self.row_diff = row_diff
        self.cards_in_row = cards_in_row

    def __click(self, x, y):
        if self.random:
            x = x + randint(-self.max_offset, self.max_offset)
            y = y + randint(-self.max_offset, self.max_offset)
        click(x, y)

    def click_set(self, game):
        # game.set_list(get_cards_from_screen())
        cards = game.get_matching_cards()
        if cards is None:
            return 1
        for card in cards:
            row = card // self.cards_in_row
            column = card % self.cards_in_row
            self.__click(self.col_first+column*self.col_diff,
                         self.row_first+row*self.row_diff)
            sleep(uniform(0.03, 0.05))
        return 0
