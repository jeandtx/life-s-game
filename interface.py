import pygame
from math import ceil


class Interface():

    def __init__(self, game) -> None:
        self.game = game
        self.running = True
        self.display = self.game.display
        self.window = self.game.window
        self.drawing = False

    def add_button(self, txt, position=(0, 0), size=(100, 50), color=(0, 0, 255),):
        button = pygame.Surface(size)
        button.fill(color)
        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        text = font.render(txt, True, (255, 255, 255))
        self.game.window.blit(button, position)
        text_position = (position[0] + ceil(size[0] / 2) - ceil(text.get_width() / 2),
                         position[1] + ceil(size[1] / 2) - ceil(text.get_height() / 2))
        self.game.window.blit(text, text_position)
        return position, size

    def round_position(self, position):
        if position % 10 != 0:
            return position - position % 10
        return position

    def click_on_button(self, click, button):
        if click[0] >= button[0][0] and click[1] >= button[0][1] and click[0] <= button[0][0] + button[1][0] and click[1] <= button[0][1] + button[1][1]:
            return True
        return False

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Stopping the Game")
                pygame.quit()
                quit()
                # self.running = False
                # error not a clean stop but it works
            elif event.type == pygame.MOUSEBUTTONUP:
                self.drawing = False
                if self.click_on_button(event.pos, self.start):
                    self.running = not self.running
                    if self.running:
                        self.initialisation()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.drawing = True

            if self.drawing and not self.click_on_button(event.pos, self.start):
                self.game.cells.create_cell(
                    (
                        self.round_position(
                            event.pos[0]), self.round_position(event.pos[1])
                    )
                )
                self.game.cells.cells_position.append(
                    (
                        self.round_position(
                            event.pos[0]), self.round_position(event.pos[1])
                    )
                )
                self.game.window.blit(
                    self.game.cells.cell, self.game.cells.cell_position)
                pygame.display.update()

    def initialisation(self):
        while self.running:
            self.check_events()
            self.start = self.add_button(
                "Start", (500, 500), (100, 50), (15, 60, 29))
            pygame.display.update()
        self.drawing = False
        self.add_button("Stop", (500, 500), (100, 50), (255, 0, 0))
        pygame.display.update()
