from typing import List
from stage import Stage


class StageManager:
    def __init__(self):
        self.__stage_list: List[Stage] = []
        self.__current_stage_idx = 0
    
    def push_stage(self, stage: Stage):
        self.__stage_list += [stage]

    @property
    def current_stage(self):
        return self.__stage_list[self.__current_stage_idx]