from time import sleep

from pynput import keyboard


class Controller:
    """Controller class for game input handling"""

    def __init__(self):
        self.keyboard = keyboard.Controller()

    def skillcheck(self, delay=0):
        """Send commands to perform the skillcheck in game"""
        sleep(delay)
        self.keyboard.press(keyboard.Key.space)
        self.keyboard.release(keyboard.Key.space)
