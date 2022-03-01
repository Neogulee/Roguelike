import os
from typing import Dict, List, Any
from xml.etree.ElementTree import ElementTree, Element


from enemy import Enemy
from enemy_behavior import EnemyBehavior
from file_reader import FileReader
from singleton_type import SingletonType
from sprite import Sprite


class EnemyFactory(metaclass=SingletonType):
    def __init__(self):
        self.__enemy_dict: Dict[str, Enemy] = {}
        self.__init_enemy_dict()
    
    def __init_enemy_dict(self):
        file_reader: FileReader = FileReader()
        for enemy in file_reader.get_element_list("enemy"):
            enemy_dict: Dict[str, Any] = {}

            name: str = enemy.find("name").text
            hp: int = int(enemy.find("hp").text)
            power: int = int(enemy.find("power").text)

            sprite_element: Element = enemy.find("sprite")
            ch: str = sprite_element.find("ch").text
            # image
            sprite: Sprite = Sprite(ch)
            
            # TODO: EnemyBehaviorfactory
            # enemy_dict["behavior"]: EnemyBehavior = 
            # on_create
            # on_destroy

            def init(self, x: int, y: int):
                super(Enemy, self).__init__(
                    sprite=sprite,
                    x=x,
                    y=y,
                    name=name,
                    max_hp=hp,
                    # behavior=None, # test
                    # on_create=None
                )

            class_name: str = enemy.get("class_name")
            self.__enemy_dict[class_name] = type(class_name, (Enemy,), {"__init__": init})

    def get_enemy(self, class_name: str, x: int, y: int) -> Enemy:
        if class_name not in self.__enemy_dict:
            raise
        return self.__enemy_dict[class_name](x, y)


if __name__ == "__main__":
    enemy_factory = EnemyFactory()
    slime: Enemy = enemy_factory.get_enemy("Slime", 0, 0)
    print(slime)
    print(slime.hp)
    print(isinstance(slime, Enemy))

