import pygame
import cells


class Game():

    def __init__(self) -> None:
        pygame.init()
        self.running = True
        self.playing = True
        self.DISPLAY_W = 1100
        self.DISPLAY_H = 1000
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        pygame.display.set_caption("Game's life")
        self.window = pygame.display.set_mode(
            ((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = pygame.font.get_default_font()
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.BLACK = (0, 0, 0)
        self.round = 0

        self.cells = cells.Cells(self)

    def game_loop(self):
        self.display.fill(self.BLACK)
        self.window.blit(self.display, (0, 0))
        self.cells.initialisation()
        while self.playing:
            self.check_events()
            self.clock.tick(self.FPS)
            self.cells.round()
            # pygame.time.wait(1000)
            pygame.display.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                # pygame.quit()
                # quit()
