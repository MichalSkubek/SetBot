from Classes.Game import Game
from ScreenClicker import ScreenClicker
from ScreenReader import ScreenReader
from time import sleep
import pyautogui

if __name__ == "__main__":
    clicker = ScreenClicker()  # Screen Clicker with default parameters
    # keyboard.add_hotkey('ctrl+q', lambda: quit(0))
    game = Game()
    if str(input('A-Auto M-Manual: ')) == 'A':
        in_row = 0
        while True:
            game.set_list(ScreenReader().get_cards_from_screen())
            x = clicker.click_set(game)
            if x == 1:
                in_row += 1
            else:
                in_row = 0
            sleep(0.05)
            pyautogui.moveTo(300, 150, 0.02)
            if in_row == 10:
                break

    else:
        print("(ROW, COLUMN), starting with 1")
        while str(input('\t> Q -> LEAVE\n\t> ENTER -> NEW SET\n')) != 'q':
            game.set_list(ScreenReader().get_cards_from_screen())
            cards = game.get_matching_cards()
            print('#', end=" ")
            if cards is None:
                continue
            for card in cards:
                print(f"{card}>({card//3 + 1}, {card%3 + 1})", end=" ")
            print("")
