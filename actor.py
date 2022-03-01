from sprite import Sprite
from game_map import GameMap
import util


class Actor:
    def __init__(self, sprite: Sprite, x: int, y: int, name: str):
        self.__sprite: Sprite = sprite
        self.__x: int = x
        self.__y: int = y

    def update(self):
        pass
        
    def x_move(self, game_map: GameMap, dx: int) -> int:
        # TODO: GameMap -> Stage
        for i in range(abs(dx)):
            next_x: int = self.__x + int(util.sign(dx))
            if game_map.get_tile(next_x, self.__y).is_wall:
                return i
            self.__x = next_x

    def y_move(self, game_map: GameMap, dy: int) -> int:
        # TODO: GameMap -> Stage
        for i in range(abs(dy)):
            next_y: int = self.__y + int(util.sign(dy))
            if game_map.get_tile(self.x, next_y).is_wall:
                return i
            self.__y = next_y

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        if x < 0:
            raise
        self.__x = x

    @property
    def y(self) -> int:
        return self.__y
    
    @y.setter
    def y(self, y: int):
        if y < 0:
            raise
        self.__y = y

    @property
    def sprite(self) -> Sprite:
        return self.__sprite

    @property
    def pos(self) -> (int, int):
        return self.__x, self.__y
    
    @pos.setter
    def pos(self, pos: (int, int)):
        self.__x, self.__y = pos
