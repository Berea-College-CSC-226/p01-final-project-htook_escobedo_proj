
import pygame
from p01_player import Player

class Game:
    def __init__(self):
        self.size = 800, 600
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)

        self.clock = pygame.time.Clock()
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill('#9CBEBA')
            pygame.display.flip()
            self.clock.tick(60)


def main():
    game = Game()
    game.run()
main()