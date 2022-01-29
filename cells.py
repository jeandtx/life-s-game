import pygame


class Cells():

    def __init__(self, game) -> None:
        self.number = 30
        self.game = game
        self.cells_position = []
        self.cell_size = (10, 10)  # Pixels
        self.x_distance = 0
        self.y_distance = 10

    def is_close_to(self, position1, position2):
        if position1[0] == position2[0] and position1[1] == position2[1]:
            return False
        elif abs(position1[0] - position2[0]) == self.x_distance or abs(position2[0] - position1[0]) == self.x_distance or abs(position1[1] - position2[1]) == self.y_distance or abs(position2[1] - position1[1]) == self.y_distance:
            return True
        return False

    def round(self):
        """
        (- If update is null then stop adding rounds ?)
            This is not in the rules but interesting to see how to code it
        todo for now it only delete the cells there is no creation
        """

        self.game.round += 1
        print(self.game.round)
        for cell in self.cells_position:
            close_to = []
            for j in range(len(self.cells_position)):
                if self.is_close_to(cell, self.cells_position[j]):
                    close_to.append(self.cells_position[j])
            if len(close_to) > 3 or len(close_to) < 2:
                self.delete_cell(cell)

    def delete_cell(self, position):
        self.cells_position.remove(position)
        self.create_cell(position, True)
        self.game.window.blit(self.cell, self.cell_position)
        pygame.display.update()

    def create_cell(self, position, dark=False):
        self.cell_position = pygame.Rect(position, self.cell_size)
        self.cell = pygame.Surface(self.cell_size)
        if dark:
            self.cell.fill((0, 0, 0))
        else:
            self.cell.fill((255, 255, 255))
        return position

    def initialisation(self):
        """
        todo implement a draw to personalize initialisation
        """

        for i in range(self.number):
            self.cells_position.append(
                self.create_cell((i*self.x_distance + 350, i*self.y_distance + 350)))
            self.game.window.blit(self.cell, self.cell_position)
            pygame.display.update()
