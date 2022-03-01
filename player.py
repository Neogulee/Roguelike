from character import Character
from sprite import Sprite


class Player(Character):
    def __init__(self, x: int, y: int, max_hp: int):
        sprite = Sprite("@")
        super().__init__(sprite=sprite, x=x, y=y, name="player", max_hp=max_hp) # test
    
        