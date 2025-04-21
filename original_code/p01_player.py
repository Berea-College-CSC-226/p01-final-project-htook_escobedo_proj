

import pygame


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
        self.rect.move_ip(self.screen_size[0]//2, self.screen_size[1]//2)

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
        Entity.position = [100, 100]
class Player(Entity):
    def __init__(self, screen_size):
        super().__init__(screen_size)
        Entity.position = [0, 0]


    def npcmovement(self,):
        """This is the movement for the npc which makes it randomly use different movements
        to reach the player. """
        pass

#
# class Player(Entity):
#     """This will differinciate the player on the screen which is controllable to
#     the user compared to the npc."""
#
#
# pass
