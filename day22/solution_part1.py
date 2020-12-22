from queue import Queue

from read_file.read_file import read_file

if __name__ == '__main__':
    lines = read_file("input.txt")

    iterator = iter(lines)
    def parse_cards():
        cards = Queue()
        next(iterator)
        while card := next(iterator):
            cards.put(int(card))
        return cards

    active_deck = parse_cards()
    other_deck = parse_cards()

    while not active_deck.empty() and not other_deck.empty():
        active_card = active_deck.get()
        other_card = other_deck.get()
        if active_card > other_card:
            active_deck.put(active_card)
            active_deck.put(other_card)
        else:
            other_deck.put(other_card)
            other_deck.put(active_card)

        active_deck, other_deck = other_deck, active_deck

    winner_deck = active_deck if not active_deck.empty() else other_deck
    score = 0
    while not winner_deck.empty():
        multiplier = winner_deck.qsize()
        card = winner_deck.get()
        score += multiplier * card

    print(f"Part 1: {score}")
