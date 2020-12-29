#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------
# Реализуйте функцию best_hand, которая принимает на вход
# покерную "руку" (hand) из 7ми карт и возвращает лучшую
# (относительно значения, возвращаемого hand_rank)
# "руку" из 5ти карт. У каждой карты есть масть(suit) и
# ранг(rank)
# Масти: трефы(clubs, C), пики(spades, S), червы(hearts, H), бубны(diamonds, D)
# Ранги: 2, 3, 4, 5, 6, 7, 8, 9, 10 (ten, T), валет (jack, J), дама (queen, Q), король (king, K), туз (ace, A)
# Например: AS - туз пик (ace of spades), TH - дестяка черв (ten of hearts), 3C - тройка треф (three of clubs)

# Задание со *
# Реализуйте функцию best_wild_hand, которая принимает на вход
# покерную "руку" (hand) из 7ми карт и возвращает лучшую
# (относительно значения, возвращаемого hand_rank)
# "руку" из 5ти карт. Кроме прочего в данном варианте "рука"
# может включать джокера. Джокеры могут заменить карту любой
# масти и ранга того же цвета, в колоде два джокерва.
# Черный джокер '?B' может быть использован в качестве треф
# или пик любого ранга, красный джокер '?R' - в качестве черв и бубен
# любого ранга.

# Одна функция уже реализована, сигнатуры и описания других даны.
# Вам наверняка пригодится itertools.
# Можно свободно определять свои функции и т.п.
# -----------------

class PockerSizeHandError(ValueError):
    pass

def hand_rank(hand):
    """Возвращает значение определяющее ранг 'руки'"""
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return 8, max(ranks)
    elif kind(4, ranks):
        return 7, kind(4, ranks), kind(1, ranks)
    elif kind(3, ranks) and kind(2, ranks):
        return 6, kind(3, ranks), kind(2, ranks)
    elif flush(hand):
        return 5, ranks
    elif straight(ranks):
        return 4, max(ranks)
    elif kind(3, ranks):
        return 3, kind(3, ranks), ranks
    elif two_pair(ranks):
        return 2, two_pair(ranks), ranks
    elif kind(2, ranks):
        return 1, kind(2, ranks), ranks
    else:
        return 0, ranks


CARD = 0
SUIT = 1


class PockerHand():
    def __init__(self, hand):
        self.hand_size = 7
        self.ranks = []
        self.card_rank = 'AKQJT98765432'
        self.hand = hand.split()

        if len(self.hand) != self.hand_size:
            raise PockerSizeHandError(self.hand)
        self.sort_hand()

    def sort_hand(self):
        new_hand = []
        for rank in self.card_rank:
            for card in self.hand:
                if card in new_hand:
                    continue
                if card[CARD] == rank:
                    new_hand.append(card)
        print('Old hand: {}'.format(self.hand))
        print('New hand: {}\r\n'.format(new_hand))
        self.hand = new_hand

    def card_ranks(self):
        """Возвращает список рангов (его числовой эквивалент),
        отсортированный от большего к меньшему"""

        street = self.check_street()
        if street:
            print('Find street index on {}, size {} '.format(street[1], street[0]))

        # Роял флеш: от 10 до Туза
        # Стрит флэш: Пять последовательных карт одной масти
        # Каре: Четыре карты одного достоинства
        # Фулл-хаус: Три карты одного достоинства и два другого
        # Флеш: Сочетание из пяти карт одной масти(не по старшенству)
        # Стрит: Пять карт подряд разной масти, но поочередного достоинства
        # Сет: Три карты одного достоинства
        # Две пары: Две пары карт одинакого достоинства
        # Пара: Две карты одинакого достоинства
        # Старшая карта: Сравнение по старшей карте

        return

    def check_street(self):
        streets = []

        start_pos = 0
        cards_count = 0
        card_index = 0
        for card in self.hand:
            current_card = str(card[CARD])

            card_pos = self.card_rank.find(current_card, 0, len(self.card_rank)-4)
            if card_pos == -1:
                break

            try:
                if self.hand[card_index+1][CARD] == self.card_rank[card_pos+1]:
                    cards_count += 1

                    if start_pos == 0:
                        start_pos = card_index
            except IndexError:
                break
            card_index += 1

        if cards_count >= 5:
            streets.append(start_pos)

        return (cards_count, streets[0]) if len(streets) > 0 else False


    def flush(self):
        """Возвращает True, если все карты одной масти"""
        return


def straight(ranks):
    """Возвращает True, если отсортированные ранги формируют последовательность 5ти,
    где у 5ти карт ранги идут по порядку (стрит)"""
    return


def kind(n, ranks):
    """Возвращает первый ранг, который n раз встречается в данной руке.
    Возвращает None, если ничего не найдено"""
    return


def two_pair(ranks):
    """Если есть две пары, то возврщает два соответствующих ранга,
    иначе возвращает None"""
    return


def best_hand(hand):
    """Из "руки" в 7 карт возвращает лучшую "руку" в 5 карт """
    return


def best_wild_hand(hand):
    """best_hand но с джокерами"""
    return


def test_best_hand():
    print("test_best_hand...")
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    print('OK')


def test_best_wild_hand():
    print("test_best_wild_hand...")
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    print('OK')


if __name__ == '__main__':
    test1 = PockerHand("6C 7C 8C 9C TC 5C JS")
    test1.card_ranks()

    test2 = PockerHand("TD TC TH 7C 7D 8C 8S")
    test2.card_ranks()


    # test_best_hand()
    # test_best_wild_hand()
