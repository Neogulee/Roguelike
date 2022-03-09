from abc import abstractmethod

from enemy_factory import EnemyFactory
from stage import Stage
from tile_factory import TileFactory


class StageGenerator:
    def __init__(self):
        self._enemy_factory: EnemyFactory = EnemyFactory()
    
    @abstractmethod
    def create_stage(self):
        pass
    

class TestStageGenerator():
    def create_stage(self) -> Stage:
        pass
