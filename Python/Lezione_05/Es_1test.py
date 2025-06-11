def blackjack_hand_total(cards: list[int]) -> int:
    totale: int = sum(cards)
    while totale > 21 and 11 in cards:
        totale = totale - 10
        cards.remove(11)
    return totale
