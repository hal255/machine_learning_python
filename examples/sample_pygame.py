"""
Pygame sample project

@author: Hong Luu
Last Update: 2018-04-26

"""

import pygame
import sys
import time

class MyPygame:

    def play_game(self):
        pygame.init()
        runGame = True

        FPS = 30
        FPS_CLOCK = pygame.time.Clock()

        # COLOR LIST
        WHITE = pygame.Color(255, 255, 255)
        GREEN = pygame.Color(0, 255, 0)

        # Code to create the initial window
        screen_w = 640
        screen_h = 480
        window_size = (screen_w, screen_h)
        SCREEN = pygame.display.set_mode(window_size)

        # set the title of the window
        pygame.display.set_caption("Hello PyGame")

        # controls the day and night values
        dayOrNight = 1  # goes from night to day when 1,
        # goes from day to night when -1
        whiteValue = 255  # BG color value that changes night or day

        # python time object to find difference of start time and current time
        startTime = time.time()

        print("generating image")

        while runGame:  # <--- main game loop
            pygame.init()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # QUIT event to exit the game
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    runGame = False


if __name__ == "__main__":
    tester = MyPygame()
    tester.play_game()
