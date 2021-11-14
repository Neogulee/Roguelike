import abc


class Tile:
    @abc.abstractmethod
    def __init__(self, name: str, description: str, char: str):
        self.__name: str = name
        self.__description: str = description
        self.__char: str = char


class SimpleTile(Tile):
    def __init__(self):
        super().__init__("Simple Tile", "This is simple tile for test", "#")