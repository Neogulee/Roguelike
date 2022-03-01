from camera import Camera
from game_controller import GameController
from screen import Screen, TerminalScreen
from view import View, TerminalView


def run():
    screen: Screen = TerminalScreen() # terminal
    camera: Camera = Camera()
    view: View = TerminalView(screen=screen, camera=camera) # terminal
    game_controller: GameController = GameController(screen=screen, view=view)
    
    try:
        game_controller.run()
    finally:
        screen.close()