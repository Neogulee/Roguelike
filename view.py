from typing import List
from abc import abstractmethod
from game_map import GameMap
from camera import Camera
from sprite import Sprite, NEW_LINE_SPRITE
from character import Character
from screen import Screen
from singleton_type import SingletonType
from stage import Stage


class View(metaclass=SingletonType):
    def __init__(self, screen: Screen, camera: Camera):
        self._screen = screen
        self._camera: Camera = camera

    @abstractmethod
    def draw(self, stage: Stage) -> None:
        pass

    
class TerminalView(View):
    def draw(self, stage: Stage, x: int, y: int) -> None:
        viewport: List[List[Sprite]] = self._camera.get_viewport(stage=stage, x=x, y=y)

        self._screen.start_drawing()
        for y, row in enumerate(viewport):
            for x, cell in enumerate(row):
                self._screen.draw(x=x, y=y, sprite=cell)
        self._screen.finish_drawing()
