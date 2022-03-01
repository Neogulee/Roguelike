import abc
import tile
from typing import List

from tile import Tile


class MapGenStrategy:
    def __init__(self):
        pass
    
    @abc.abstractmethod
    def execute(self) -> (int, int, List[List[Tile]]):
        pass


class GameMap:
    def __init__(self, map_gen_strategy: MapGenStrategy):
        ret = map_gen_strategy.execute()
        self.__width: int = ret[0]
        self.__height: int = ret[1]
        self.__tiles: List[List[Tile]] = ret[2]

    def get_tile(self, x: int, y: int) -> Tile:
        return self.__tiles[y][x]

    def get_tiles(self, top: int, bottom: int, left: int, right: int)\
            -> List[List[Tile]]:
        top = max(0, top)
        bottom = min(self.__height - 1, bottom)
        left = max(0, left)
        right = min(self.__width - 1, right)
        return [row[left:right + 1] for row in self.__tiles[top:bottom + 1]]

    @property
    def width(self) -> int:
        return self.__width
    
    @property
    def height(self) -> int:
        return self.__height


class TestMapGenStrategy(MapGenStrategy):
    def execute(self) -> (int, int, List[List[Tile]]):
        width: int = 30
        height: int = 20
        tiles: List[List[Tile]] = [[tile.TestTile() for i in range(width)] for j in range(height)]
        for i in range(height):
            tiles[i][0] = tile.TestTile2()
            tiles[i][width - 1] = tile.TestTile2()
        for i in range(width):
            tiles[0][i] = tile.TestTile2()
            tiles[height - 1][i] = tile.TestTile2()
        return width, height, tiles