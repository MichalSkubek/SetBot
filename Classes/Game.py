from .Card import Card


class Game:
    def __init__(self):
        self.cards = list()

    def get_matching_cards(self):
        cards_len = len(self.cards)
        for i in range(cards_len):
            for j in range(i + 1, cards_len):
                matching_card = self.cards[i].match_card(self.cards[j])
                for k in range(j+1, cards_len):
                    if matching_card == self.cards[k]:
                        print(self.cards[i])
                        print(self.cards[j])
                        print(self.cards[k])
                        #print(f"({i//3 + 1} {i%3 + 1}) ({j//3 + 1} {j%3 + 1}) ({k//3 + 1} {k%3 + 1})")
                        return i, j, k
        return

    def add_card(self, color, shape, texture, number):
        self.cards.append(Card(color, shape, texture, number))

    def set_list(self, cards):
        self.cards.clear()
        self.cards = cards
        # for card in cards:
        #     print(card)
