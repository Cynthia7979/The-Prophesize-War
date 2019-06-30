# -*- coding: gb2312 -*-
from .global_variable import *


class Hand:
    def __init__(self, cards:tuple=()):
        self.cards = list(cards)

    def get_cards(self):
        return self.cards


class Card:
    """
    ����
    ϡ�ж�
    ��ǩ
    ����
    ����
    Ч��
    ���棿/���棿
    """
    _name: str  # ����
    _type: str
    _rarity: int
    _tag: [str]
    _description: str  # ��������
    _effect_description: str  # Ч������
    _effect_ID: str  # Ч��ID

    def __init__(self, name: str, type: str, rarity: int, tag: [str], description: str,
                 effect_description: str, effect_id: str):
        self._name = name
        self._type = type
        self._rarity = rarity
        self._tag = tag
        self._description = description
        self._effect_description = effect_description
        self._effect_ID = effect_id
        self.image = image('resources/fake_card.png', resize=(CARD_WIDTH, CARD_HEIGHT))


class ItemCard(Card):
    """
    ���߿�
    """

    def __init__(self, name: str, type: str, rarity: int, tag: [str], description: str,
                 effect_description: str, effect_id: str):
        Card.__init__(self, name, type, rarity, tag, description, effect_description, effect_id)


class RitualCard(Card):
    """
    ��ʽ��
    """

    def __init__(self, name: str, type: str, rarity: int, tag: [str], description: str,
                 effect_description: str, effect_id: str):
        Card.__init__(self, name, type, rarity, tag, description, effect_description, effect_id)

    def get_effect_id(self):
        return self._effect_ID


