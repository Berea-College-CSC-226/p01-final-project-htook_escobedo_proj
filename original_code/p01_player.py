

import pygame
import random
"hello2"
class Entity(pygame.sprite.Sprite):

    """This class represents the entity on the screen"""
    def __init__(self, screen_size):
        """
        :param
        screen_size: Screen size, for keeping character on the screen
        """
        super().__init__()
        self.screen_size = screen_size
        print("Game Starting")
        self.surf = pygame.image.load('Player.PNG').convert_alpha()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()


    def p1movement(self, keys):
        """
        This def makes the user able to control the player sprite with the keyboard keys.

        Handles up, down, left, right movement events from the user

        :param keys: key presses from pygame event listener
        :return: None
        """
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -3)
        elif keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 3)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(3, 0)
        elif keys[pygame.K_LEFT]:
            self.rect.move_ip(-3, 0)

class Mob(Entity):
    """This will differinciate the NPC on the screen which moves randombly
    and is actively tring to reach the player, from the actual player. """
    def __init__(self, screen_size):
        super().__init__(screen_size)
        self.surf = pygame.image.load('Shocked.mob.png').convert_alpha()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.screen_size[0]*3//4, self.screen_size[1]*3//4)
        self.move_distance = 20
        self.directions = ["north", "east", "west", "south"]
        self.path = random.choices(self.directions)
        # Entity.position = [100, 100]
    def npc_directions(self):

        if self.rect.bottom >= self.screen_size[1]:
            # Bottom
            self.path = "north"
        if self.rect.top <= 0:
            # Top
            self.path = "south"
        if self.rect.left <= 0:
            # Left
            self.path = "east"
        if self.rect.right >= self.screen_size[0]:
            # Right
            self.path = "west"
        elif random.random() > .95:
            # Randomly change direction 5% of the time
            self.path = random.choice(self.directions)

    def npcmovement(self,):
        """This is the movement for the npc which makes it randomly use different movements
        to reach the player. """
        if self.path == "north":
            self.rect.move_ip(0, -self.move_distance)
        elif self.path == "south":
            self.rect.move_ip(0, self.move_distance)
        elif self.path == "east":
            self.rect.move_ip(self.move_distance, 0)
        elif self.path == "west":
            self.rect.move_ip(-self.move_distance, 0)



class Player(Entity):
    def __init__(self, screen_size):
        super().__init__(screen_size)
        self.surf = pygame.image.load('Player.PNG').convert_alpha()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.screen_size[0]//4, self.screen_size[1]//4)
        # Entity.position = [0, 0]



    def npcmovement(self,):
        """This is the movement for the npc which makes it randomly use different movements
        to reach the player. """
        if self.path == "north":
            self.rect.move_ip(0, -self.move_distance)
            self.position[1] -= self.move_distance
        elif self.path == "south":
            self.rect.move_ip(0, self.move_distance)
            self.position[1] += self.move_distance
        if self.path == "east":
            self.rect.move_ip(self.move_distance, 0)
            self.position[0] -= self.move_distance
        if self.path == "west":
            self.rect.move_ip(-self.move_distance, 0)
            self.position[0] += self.move_distance

        self.npc_directions()

#
# class Player(Entity):
#     """This will differinciate the player on the screen which is controllable to
#     the user compared to the npc."""
#
#
# pass
