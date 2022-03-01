from __future__ import annotations

from actor import Actor
from sprite import Sprite


class Character(Actor):
    def __init__(self, sprite: Sprite, x: int, y: int, name: str, max_hp: int):
        super().__init__(sprite=sprite, name=name, x=x, y=y)
        self.__max_hp: int = max_hp
        self.__hp: int = max_hp

        self.__is_dead: bool = True

    def update(self):
        pass
        
    def attack(self, target: Character) -> None:
        # TODO: calculate defense and etc.
        target.take_damage(10) # value is for test
    
    def take_damage(self, amount: int) -> None:
        # TODO: calculate defense and etc.
        self.hp -= amount
        
    @property
    def max_hp(self) -> int:
        return self.__max_hp
    
    @max_hp.setter
    def max_hp(self, max_hp: int):
        if max_hp < 0:
            raise ValueError()
        self.__max_hp = max_hp

    @property
    def hp(self) -> int:
        return self.__hp

    @hp.setter
    def hp(self, hp: int):
        if hp > self.__max_hp:
            hp = self.__max_hp
        if hp <= 0:
            hp = 0
            self.__is_dead = True
        self.__hp = hp

    @property
    def is_dead(self) -> bool:
        return self.__is_dead