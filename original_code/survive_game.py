
import pygame
from p01_player import Entity, Player, Mob, Maze
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

        #Creates Player and NPC
        self.guy = Player(self.size)
        self.badguy = Mob(self.size)

        tile_size = 39
        screen_width, screen_height = self.size
        columns = screen_width // tile_size
        rows = screen_height // tile_size

        self.maze_layout = [
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # row 1
            "X              XX              X",  # row 2
            "X X XXX XXX XX  X X  XXX XXX X X",  # row 3
            "X X     X    XX   XX   X     X X",  # row 4
            "X XX XX   XX X  X XXXX XX X XX X",  # row 5
            "X     X   X    XX X    X  X  X X",  # row 6
            "X XXX   X   XXXX    X XX XXX   X",  # row 7
            "X   XXX XXXXX    X XX        X X",  # row 8
            "X X      X    XX X    XXXX XXX X",  # row 9
            "X XXX  X    X  X X XX  X    X  X",  # row 10
            "X   XX XXX XXX      XX   XX    X",  # row 11
            "X X      X     XX X    X X   X X",  # row 12
            "X X XX X XXX X    XXX XX X XXX X",  # row 13
            "X X    X     XX X          X   X",  # row 14
            "X XXX XXXX XXXX XXX XXXXXX X X X",  # row 15
            "X                              X",  # row 16
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # row 17
        ]

        self.walls = pygame.sprite.Group()
        for row_idx, row in enumerate(self.maze_layout):
            for col_idx, tile in enumerate(row):
                if tile == "X":
                    x = col_idx * tile_size
                    y = row_idx * tile_size
                    self.walls.add(Maze(x, y, tile_size, tile_size))


    # Add GUI in here that then calls run after quiting.
    def game_over(self):
        """This creates game over screen after the pygame event ends because they aren't able to work together to
        a seperate function is required to show this"""
        game_over_window = tk.Toplevel()
        game_over_window.configure(bg="#1e1e2f")  # Light blue background
        game_over_window.title("Game Over")


        window_width = 400
        window_height = 250
        # Get the screen dimensions
        screen_width = game_over_window.winfo_screenwidth()
        screen_height = game_over_window.winfo_screenheight()

        # Calculate the position to center the window
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set the geometry of the window
        game_over_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        game_over_window.resizable(False, False)

        label = tk.Label(
            game_over_window,
            text="You Win!!!",           #The text displayed
            font =("Comic Sans MS", 16), #The font and size
            bg = "#1e1e2f",              #The background color
            fg = "white",                #The text color
            pady = 20
        )
        label.pack()

        button_style = {
            "font": ("Comic Sans MS", 16),
            "bg": "#444",  # Button background
            "fg": "#FFF",  # Text color
            "activebackground": "#666",  # Background when hovered
            "activeforeground": "#FFD700",  # Text color when hovered
            "width": 12,
            "relief": "raised",
            "bd": 3
        }

        restart_button = tk.Button(
            game_over_window,
            text="Restart?",
            command=lambda: [game_over_window.destroy(), self.restart()],
            **button_style
        )
        restart_button.pack(pady=5)

        exit_button = tk.Button(game_over_window, text= "Exit",
                                command=lambda: [game_over_window.destroy(), pygame.quit(), sys.exit()],
                                bg="red", fg="black") #Creates an exit button
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
            self.badguy.npcmovement(self.walls)
            self.screen.fill('#9CBEBA')
            seconds = (pygame.time.get_ticks() - self.start_time) / 1000
            # self.screen.fill((60, 20, 30))
            timer_text = self.font.render(f"Score: {seconds:.2f}s", True, (255, 255, 255))
            self.screen.blit(timer_text, (0, 0))

            if not pygame.sprite.spritecollide(self.badguy, [self.guy], False):
                self.guy.p1movement(self.walls)
                self.screen.fill('#9CBEBA')
                self.walls.draw(self.screen)
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




    def scoreboard(self):
        """This will use the time funtion to get the score, everytime time goes up
        so does the score. """

        pass


def main():
    game = Game()
    game.run()

if __name__ == '__main__':
    main()