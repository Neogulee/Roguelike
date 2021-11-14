import abc
import tile


class GameMap:
    def __init__(self):
        self.__width: int = 0
        self.__height: int = 0
        self.__tiles: list[list[tile.Tile]] = []

    @abc.abstractmethod
    def generate_map(self) -> None:
        pass

    def get_tile(self, y: int, x: int) -> tile.Tile:
        return self.__tiles[y][x]

    @property
    def width(self) -> int:
        return self.__width
    
    @property
    def height(self) -> int:
        return self.__height
