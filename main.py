from game import Game

if __name__ == "__main__":
    g = Game()
    print("Starting the Game")
    while g.running:
        g.game_loop()
    print("Ending the Game")
