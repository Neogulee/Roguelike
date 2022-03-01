from tile import Tile
from file_reader import FileReader
from singleton_type import SingletonType
from sprite import Sprite


class TileFactory(metaclass=SingletonType):
    def get_tile(self, class_name: str) -> Tile:
        pass
