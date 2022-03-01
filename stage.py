from game_map import GameMap, TestMapGenStrategy
from typing import List
from character import Character


class Stage:
    def __init__(self, game_map: GameMap):
        self.__game_map: GameMap = game_map
        self.__character_grid: List[List[Character]] = []
        self.__character_list: List[Character] = []
    
    def add_character(self, character: Character, x: int, y: int) -> None:
        # TODO: exception
        
        self.__character_list += [character]
        # self.__character_grid[x][y] = character
        character.pos = x, y

    @property
    def width(self) -> int:
        return self.__game_map.width

    @property
    def height(self) -> int:
        return self.__game_map.height

    @property
    def game_map(self) -> GameMap:
        return self.__game_map
    
    @property
    def character_list(self) -> List[Character]:
        return self.__character_list


test_stage = Stage(GameMap(TestMapGenStrategy())) # temp