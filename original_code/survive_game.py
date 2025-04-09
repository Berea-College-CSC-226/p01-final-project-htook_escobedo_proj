import pygame

class Game:
    """
#This will be where all the code for the game is housed.
This is the setup for the screen

    """
    def __init__(self):
        self.size = 800, 600
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)

        self.clock = pygame.time.Clock()

    def run(self):

        """

        This will run the actual code.
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill('#9CBEBA')
            pygame.display.flip()
            self.clock.tick(60)

    def death(self, other):
        """" This is for when the player collides with the npc,
            if they do the game will be over
            and it will display a message before restarting the game.
            """


        pass

    def maze(self):
        """This would require a turtle to make the overall layout for the maze"""

        pass



    def time:
    """This counts the time until death function is triggered"""

        pass
    def scoreboard(self):
        """This will use the time funtion to get the score, everytime time goes up
        so does the score. """

        pass


def main():
    game = Game()
    game.run()
main()