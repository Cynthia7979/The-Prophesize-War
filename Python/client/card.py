# -*- coding: gb2312 -*-


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
    # _fg_image: #ǰ��ͼƬ
    # _bg_image: #����ͼƬ
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
