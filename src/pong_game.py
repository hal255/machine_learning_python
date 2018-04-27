"""
    pong_game is a sample pong game to run with user vs AI with Machine Learning
"""

import pygame
import pathlib

assets_folder = pathlib.Path('assets')

DEBUG = True

class PongGame:
    def __init__(self):
        self._running = True
        # self._display_surf = None
        # self.size = self.weight, self.height = 640, 400
        # self.player_image = assets_folder.joinpath('images').joinpath('green_bar.png')
        self.screen_size = self.screen_width, self.screen_height = 640, 400
        self.screen = pygame.display.set_mode(self.screen_size)
        self.background = assets_folder.joinpath('images').joinpath('pink_screen.png')

    # def on_init(self):
    #     pygame.init()
    #     self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
    #     self._running = True
    #
    # def on_event(self, event):
    #     if event.type == pygame.QUIT:
    #         self._running = False
    #
    # def on_loop(self):
    #     pass
    #
    # def on_render(self):
    #     pass
    #
    # def on_cleanup(self):
    #     pygame.quit()

    # play_game function is the main function for PongGame
    # displays game
    def play_game(self):

        while self._running:

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if DEBUG:
                        print('mouse down detected')
                    self._running = False
            background = str(self.background)
            print(background)
            self.load_image(background)

    def load_image(self, image):
        pygame.image.load(image)


if __name__ == '__main__':
    game = PongGame()
    game.play_game()
