# -*- coding: gb2312 -*-

from .spirit import Spirit


class Human:
    """

    """
    _name: str
    _luck: int  # ����ֵ
    _spirit_on_body: [Spirit]  # ������������


class NPC(Human):

    _fate: int  # ����ֵ

    # mission: Mission #��������


class Player(Human):
    """
    ���
����
����
����
����NPC
�ѽ�����

    """
    _coin: int
    _prestige: int
    _owned_npc: []  # class: NPC
    _hand: []       # class: Card
    _score: int
    # mission: []
