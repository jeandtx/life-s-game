import pygame


class Cells():

    def __init__(self, game) -> None:
        self.number = 4
        self.game = game
        self.cells_position = []
        self.cell_size = (10, 10)  # Pixels
        self.x_distance = 10
        self.y_distance = 10
        self.mem = []

    def is_close_to(self, position1, position2):
        if position1[0] == position2[0] and position1[1] == position2[1]:
            return False
        elif abs(position1[0] - position2[0]) <= self.x_distance and abs(position1[1] - position2[1]) <= self.y_distance:
            return True
        return False

    def display_round(self):
        self.game.round += 1
        block = pygame.Surface((50, 20))
        block.fill((0, 0, 0))
        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        text = font.render("Round: " + str(self.game.round),
                           True, (255, 255, 255))
        self.game.window.blit(block, (80, 10))
        self.game.window.blit(text, (10, 10))

    def born(self, position):
        ctr = 0
        for cell in self.cells_position:
            if self.is_close_to(cell, position):
                ctr += 1
        if ctr == 3:
            return True
        return False

    def create_cells(self):
        cells_position = []
        for cell in self.cells_position:
            to_check = [(cell[0] + self.x_distance, cell[1]),
                        (cell[0] - self.x_distance, cell[1]),
                        (cell[0], cell[1] + self.y_distance),
                        (cell[0], cell[1] - self.y_distance),
                        (cell[0] + self.x_distance, cell[1] + self.y_distance),
                        (cell[0] - self.x_distance, cell[1] + self.y_distance),
                        (cell[0] + self.x_distance, cell[1] - self.y_distance),
                        (cell[0] - self.x_distance, cell[1] - self.y_distance)]
            print("to check", to_check)
            for check in to_check:
                if self.born(check) and check not in cells_position:
                    self.create_cell(check)
                    cells_position.append(check)
                    self.game.window.blit(self.cell, self.cell_position)
        return cells_position

    def delete_cells(self):
        to_delete = []
        for cell in self.cells_position:
            close_to = []
            for j in range(len(self.cells_position)):
                if self.is_close_to(cell, self.cells_position[j]):
                    close_to.append(self.cells_position[j])
            print(cell, "is close to", close_to)
            if len(close_to) > 3 or len(close_to) < 2:
                to_delete.append(cell)
        for cell in to_delete:
            self.delete_cell(cell)

    def check_duplicate(self):
        self.cells_position = list(dict.fromkeys(self.cells_position))

    def round(self):
        """
        (- If update is null then stop adding rounds ?)
            This is not in the rules but interesting to see how to code it
        """
        print(self.cells_position)
        self.display_round()
        temp = self.create_cells()
        self.delete_cells()
        for cell in temp:
            self.cells_position.append(cell)
        self.check_duplicate()

    def delete_cell(self, position):
        self.cells_position.remove(position)
        self.create_cell(position, True)
        self.game.window.blit(self.cell, self.cell_position)
        pygame.display.update()

    def create_cell(self, position, dark=False):
        if position in self.cells_position:
            return
        self.cell_position = pygame.Rect(position, self.cell_size)
        self.cell = pygame.Surface(self.cell_size)
        if dark:
            self.cell.fill((0, 0, 0))
            print("Cell at position", position, "is dead")
        else:
            self.cell.fill((255, 255, 255))
            print("New cell at position", position)
        return position

    def initialisation(self):
        """
        todo implement a draw to personalize initialisation
        """

        # for i in range(self.number):
        #     self.cells_position.append(
        #         self.create_cell((i*0 + 350, i*self.y_distance + 350))
        #     )
        #     self.game.window.blit(self.cell, self.cell_position)
        #     pygame.display.update()

        self.cells_position.append(
            self.create_cell((350, 350))
        )
        self.game.window.blit(self.cell, self.cell_position)
        pygame.display.update()
        self.cells_position.append(
            self.create_cell((360, 340))
        )
        self.game.window.blit(self.cell, self.cell_position)
        pygame.display.update()
        self.cells_position.append(
            self.create_cell((360, 330))
        )
        self.game.window.blit(self.cell, self.cell_position)
        pygame.display.update()
        self.cells_position.append(
            self.create_cell((350, 320))
        )
        self.game.window.blit(self.cell, self.cell_position)
        pygame.display.update()
        self.cells_position.append(
            self.create_cell((340, 340))
        )
        self.game.window.blit(self.cell, self.cell_position)
        pygame.display.update()
        self.cells_position.append(
            self.create_cell((340, 330))
        )
        self.game.window.blit(self.cell, self.cell_position)
        pygame.display.update()
        self.cells_position.append(
            self.create_cell((350, 330))
        )
        self.game.window.blit(self.cell, self.cell_position)
        pygame.display.update()
