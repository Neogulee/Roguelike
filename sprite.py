import colorama


class Sprite:
    def __init__(self, ch: str, fore: str="", back: str=""):
        if len(ch) != 1:
            raise "ch size must be 1"
            
        self.__ch: str = ch
        self.__fore: str = fore
        self.__back: str = back
    
    def __str__(self):
        return self.__fore + self.__back + self.__ch + colorama.Style.RESET_ALL
    
    @property
    def colored_ch(self) -> str:
        return self.__fore + self.__back + self.__ch + colorama.Style.RESET_ALL

    @property
    def ch(self) -> str:
        return self.__ch


SPACE_SPRITE: Sprite = Sprite(" ")
NEW_LINE_SPRITE: Sprite = Sprite("\n")