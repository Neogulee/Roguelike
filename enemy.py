from typing import Callable

from character import Character
from sprite import Sprite
from enemy_behavior import EnemyBehavior


class Enemy(Character):
    def __init__(self, sprite: Sprite, x: int, y: int, name: str, max_hp: int,
            behavior: EnemyBehavior, on_create: Callable = None,
            on_destory: Callable = None
            ):
        super().__init__(self, sprite=sprite, x=x, y=y, name=name, max_hp=max_hp)
        self._behavior: EnemyBehavior = behavior
        self._on_create: Callable = on_create # move to actor or character
        self._on_destory: Callable = on_destory # =

    def update(self):
        self._behavior.take_turn()

