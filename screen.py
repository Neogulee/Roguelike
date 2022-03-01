from abc import abstractmethod
import curses
from typing import List

from singleton_type import SingletonType
from sprite import Sprite


class Screen(metaclass=SingletonType):
    @abstractmethod
    def close(self) -> None:
        pass
        
    @abstractmethod
    def get_key(self) -> str:
        pass
    
    @abstractmethod
    def start_drawing(self) -> None:
        pass
    
    @abstractmethod
    def finish_drawing(self) -> None:
        pass

    @abstractmethod
    def draw(self, x: int, y: int, sprite: Sprite) -> None:
        pass


class TerminalScreen(Screen):
    def __init__(self):
        self.__window = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.__window.keypad(True)

    def __del__(self) -> None:
        self.close()

    def close(self) -> None:
        curses.nocbreak()
        self.__window.keypad(False)
        curses.echo()
        curses.endwin()

    def get_key(self) -> str:
        return self.__window.getkey()

    def start_drawing(self) -> None:
        # self.__window.clear()
        pass

    def finish_drawing(self) -> None:
        self.__window.refresh()
        
    def draw(self, x: int, y: int, sprite: Sprite) -> None:
        self.__window.addstr(y, x, sprite.ch)
