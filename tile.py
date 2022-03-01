import abc
from sprite import Sprite
import colorama


class Tile:
    @abc.abstractmethod
    def __init__(self, sprite: Sprite, name: str, description: str, is_wall: bool):
        self.__name: str = name
        self.__description: str = description
        self.__sprite: Sprite = sprite
        self.__is_wall: bool = is_wall
    
    def __str__(self):
        return self.__sprite.__str__()

    @property
    def is_wall(self):
        return self.__is_wall

    @property
    def sprite(self):
        return self.__sprite


class TestTile(Tile):
    def __init__(self):
        super().__init__(sprite=Sprite("."), name="Test Tile",
            description="This tile is for test", is_wall=False)


class TestTile2(Tile):
    def __init__(self):
        super().__init__(sprite=Sprite("#", colorama.Fore.RED, colorama.Back.WHITE), name="Test2 Tile",
            description="This tile is for test", is_wall=True)