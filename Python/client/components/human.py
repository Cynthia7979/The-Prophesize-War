# -*- coding: gb2312 -*-


class Human:
    """

    """
    def __init__(self, name: str, luck: int):
        self.name = name
        self._luck = luck  # ����ֵ
        self._spirit = []  # ������������ class: Spirit


class NPC(Human):
    def __init__(self, name, luck):
        Human.__init__(self, name, luck)
        self._fate: int    # ����ֵ
        self.mission = []  # �������� class: Mission


class Player(Human):
    """
    ���
    ����
    ����
    ����
    ����NPC
    �ѽ�����

    """
    def __init__(self, name, id):
        Human.__init__(self, name, luck=0)
        self.coin: int
        self.prestige: int  # ����
        self.owned_npc: []  # class: NPC
        self.hand: []       # class: Card
        self.mission: []     # ����
        self.id = id
