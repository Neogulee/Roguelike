import curses

from enemy_factory import EnemyFactory
from player import Player
from screen import Screen
from stage import test_stage
from stage_manager import StageManager
from view import View


class GameController:
    def __init__(self, screen: Screen, view: View):
        self.__screen = screen
        self.__view = view
        self.__key_map = {}

        self.__player = Player(3, 4, 100) # temp
        self.__stage_manager = StageManager()
        self.__stage_manager.push_stage(test_stage)
        self.__stage_manager.current_stage.add_character(
            character=self.__player, x=self.__player.x, y=self.__player.y)
        self.__enemy_factory = EnemyFactory()

    def run(self):
        self.__view.draw(x=self.__player.x, y=self.__player.y,
            stage=self.__stage_manager.current_stage)
        while True:
            key: str = self.__screen.get_key()
            self.__process_key(key)
            self.__view.draw(x=self.__player.x, y=self.__player.y,
                stage=self.__stage_manager.current_stage)

    def __process_key(self, key: str):
        if False:
            pass
        elif key == "KEY_LEFT":
            self.__player.x_move(self.__stage_manager.current_stage.game_map, -1)
        elif key == "KEY_RIGHT":
            self.__player.x_move(self.__stage_manager.current_stage.game_map, 1)
        elif key == "KEY_UP":
            self.__player.y_move(self.__stage_manager.current_stage.game_map, -1)
        elif key == "KEY_DOWN":
            self.__player.y_move(self.__stage_manager.current_stage.game_map, 1)

