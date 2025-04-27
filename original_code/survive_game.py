
import pygame
from p01_player import Entity, Player, Mob
import sys
import tkinter as tk

class Game:
    """
#This will be where all the code for the game is housed.
This is the setup for the screen

    """
    def __init__(self):
        self.size = 1250, 680
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.font = pygame.font.SysFont(None, 40)
        self.clock = pygame.time.Clock()
        self.start_time = pygame.time.get_ticks()
        self.screen.fill('#9CBEBA')
        self.guy = Player(self.size)
        self.badguy = Mob(self.size)

    # Add GUI in here that then calls run after quiting.
    def game_over(self):
        """This creates game over screen after the pygame event ends because they aren't able to work together to
        a seperate function is required to show this"""
        game_over_window = tk.Toplevel()
        game_over_window.title("Game Over")


        window_width = 300
        window_height = 200
        # Get the screen dimensions
        screen_width = game_over_window.winfo_screenwidth()
        screen_height = game_over_window.winfo_screenheight()

        # Calculate the position to center the window
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set the geometry of the window
        game_over_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        label = tk.Label(game_over_window, text="Gameover", font =("Comic Sans MS", 16)) #sets the text, font and size
        label.pack(pady=20)
        restart_button = tk.Button(game_over_window, text="Restart", command=lambda: [game_over_window.destroy(), self.restart()])
        restart_button.pack(pady=5)

        exit_button = tk.Button(game_over_window, text= "Exit", command=lambda: [game_over_window.destroy(), pygame.quit(), sys.exit()]) #Creates an exit button
        exit_button.pack(pady=10)

        game_over_window.mainloop()

    def restart(self):
        """Reset the game state and restart."""
        self.start_time = pygame.time.get_ticks()  # Reset the timer
        self.guy = Player(self.size)  # Re-create the player
        self.badguy = Mob(self.size)  # Re-create the NPC
        self.running = True
        self.run()  # Restart the game loop

    def run(self):

        """

        This will run the actual code.
        """

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.badguy.npc_directions()
            self.badguy.npcmovement()
            self.screen.fill('#9CBEBA')
            seconds = (pygame.time.get_ticks() - self.start_time) / 1000
            # self.screen.fill((60, 20, 30))
            timer_text = self.font.render(f"Score: {seconds:.2f}s", True, (255, 255, 255))
            self.screen.blit(timer_text, (0, 0))

            if not pygame.sprite.spritecollide(self.badguy, [self.guy], False):
                self.guy.p1movement(pygame.key.get_pressed())
                self.screen.fill('#9CBEBA')
                self.screen.blit(self.guy.surf, self.guy.rect)
                self.screen.blit(self.badguy.surf, self.badguy.rect)

            else:
                self.running = False
                self.game_over()




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

if __name__ == '__main__':
    main()