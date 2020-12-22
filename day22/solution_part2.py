def play(player_1, player_2, t):
    visited = set()
    while player_1 and player_2:
        if (player_1, player_2) in visited:
            return player_1, True

        visited.add((player_1, player_2))

        player_1_card = player_1[0]
        player_2_card = player_2[0]
        player_1 = player_1[1:]
        player_2 = player_2[1:]

        if len(player_1) >= player_1_card and len(player_2) >= player_2_card:
            player_1_won_round = play(player_1[:player_1_card], player_2[:player_2_card], t + 1)[1]
        else:
            player_1_won_round = player_1_card > player_2_card

        if player_1_won_round:
            player_1 += (player_1_card, player_2_card)
        else:
            player_2 += (player_2_card, player_1_card)

    return (player_1, True) if player_1 else (player_2, False)


from read_file.read_file import read_file

if __name__ == '__main__':
    lines = read_file("input.txt")

    iterator = iter(lines)


    def parse_cards():
        cards = []
        next(iterator)
        while card := next(iterator):
            cards.append(int(card))
        return tuple(cards)


    p1 = parse_cards()
    p2 = parse_cards()

    winning_deck = play(p1, p2, 0)[0]
    score = sum((len(winning_deck) - i) * card for i, card in enumerate(winning_deck))

    print(winning_deck)
    print(f"Part 2: {score}")
