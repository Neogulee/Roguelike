from typing import List

from character import Character
from game_map import GameMap
from sprite import Sprite, SPACE_SPRITE
from stage import Stage
from tile import Tile
from util import check_out_of_range


class Camera:
    BASE_SIGHT: int = 8

    def __init__(self):
        self.__sight: int = self.BASE_SIGHT
    
    def reset_sight(self) -> None:
        self.__sight = self.BASE_SIGHT

    def get_viewport(self, stage: Stage, x: int, y: int) -> List[List[Sprite]]:
        # add tiles
        top = y - self.__sight
        bottom = y + self.__sight
        left = x - self.__sight
        right = x + self.__sight

        tiles: List[List[Tile]] = stage.game_map.get_tiles(
            top=top, bottom=bottom, left=left, right=right)
        
        top_space = [[SPACE_SPRITE] * self.length] * max(0, -top)
        bottom_space = [[SPACE_SPRITE] * self.length] * max(0, bottom - stage.height + 1)
        left_space = [SPACE_SPRITE] * max(0, -left)
        right_space = [SPACE_SPRITE] * max(0, right - stage.width + 1)

        viewport: List[List[Sprite]] = [[tile.sprite for tile in row] for row in tiles]     
        for row in viewport:
            row[:0] = left_space
            row[len(row):] = right_space
        viewport = top_space + viewport + bottom_space
        
        # add characters
        for character in stage.character_list:
            v_x = character.x - (x - self.__sight)
            v_y = character.y - (y - self.__sight)
            if not check_out_of_range(
                    min_x=0, min_y=0,
                    max_x=stage.game_map.width - 1,
                    max_y=stage.game_map.height - 1,
                    x=v_x, y=v_y):
                viewport[v_y][v_x] = character.sprite
        return viewport

    @property
    def sight(self) -> int:
        return self.__sight
    
    @sight.setter
    def sight(self, sight: int):
        self.__sight = 0 if sight < 0 else sight

    @property
    def length(self) -> int:
        return self.__sight * 2 + 1