import pygame
import sys

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
        self.font = pygame.font.SysFont(None, 40)
        self.clock = pygame.time.Clock()
        self.start_time = pygame.time.get_ticks()

    def run(self):

        """

        This will run the actual code.
        """

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill('#9CBEBA')
            seconds = (pygame.time.get_ticks() - self.start_time) / 1000
            # self.screen.fill((60, 20, 30))
            timer_text = self.font.render(f"Score: {seconds:.2f}s", True, (255, 255, 255))
            self.screen.blit(timer_text, (0, 0))
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




    def scoreboard(self):
        """This will use the time funtion to get the score, everytime time goes up
        so does the score. """

        pass


def main():
    game = Game()
    game.run()
main()