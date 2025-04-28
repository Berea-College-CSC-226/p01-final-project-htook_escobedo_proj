

import pygame
import random

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

    #
    # def p1movement(self, walls):
    #     """
    #     This def makes the user able to control the player sprite with the keyboard keys.
    #
    #     Handles up, down, left, right movement events from the user
    #
    #     :param keys: key presses from pygame event listener
    #     :return: None
    #     """
    #     keys = pygame.key.get_pressed()
    #     dx = dy = 0
    #     if keys[pygame.K_UP]:
    #         self.rect.move_ip(0, -3)
    #     elif keys[pygame.K_DOWN]:
    #         self.rect.move_ip(0, 3)
    #     if keys[pygame.K_RIGHT]:
    #         self.rect.move_ip(3, 0)
    #     elif keys[pygame.K_LEFT]:
    #         self.rect.move_ip(-3, 0)
    #
    #     self.rect.x += dx
    #     if pygame.sprite.spritecollideany(self, walls):
    #             self.rect.x -= dx
    #
    #     self.rect.y += dy
    #     if pygame.sprite.spritecollideany(self, walls):
    #             self.rect.y -= dy

class Mob(Entity):
    """This will differinciate the NPC on the screen which moves randombly
    and is actively tring to reach the player, from the actual player. """
    def __init__(self, screen_size):
        super().__init__(screen_size)
        self.surf = pygame.image.load('Shocked.mob.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (35, 35))
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.screen_size[0]*3//4, self.screen_size[1]*3//4)
        self.move_distance = 4
        self.directions = ["north", "east", "west", "south"]
        self.path = random.choice(self.directions)
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

    def npcmovement(self, walls):
        """This is the movement for the npc which makes it randomly use different movements
        to reach the player. """
        move = {
            "north": (0, -self.move_distance),
            "south": (0, self.move_distance),
            "east": (self.move_distance, 0),
            "west": (-self.move_distance, 0)
        }

        dx, dy = move[self.path]

        # Try moving
        self.rect.x += dx
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.x -= dx
            self.path = random.choice(self.directions)  # try new direction
            return

        self.rect.y += dy
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.y -= dy
            self.path = random.choice(self.directions)



class Player(Entity):
    def __init__(self, screen_size):
        super().__init__(screen_size)
        self.surf = pygame.image.load('Player.PNG').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (35, 35))
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.screen_size[0]*1//4, self.screen_size[1]*1//4)
        # Entity.position = [0, 0]


    def p1movement(self, walls):
        """
        This def makes the user able to control the player sprite with the keyboard keys.

        Handles up, down, left, right movement events from the user

        :param keys: key presses from pygame event listener
        :return: None
        """
        dx = dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dx = -3
        elif keys[pygame.K_RIGHT]:
            dx = 3
        if keys[pygame.K_UP]:
            dy = -3
        elif keys[pygame.K_DOWN]:
            dy = 3

        self.rect.x += dx
        if pygame.sprite.spritecollideany(self, walls):
                self.rect.x -= dx

        self.rect.y += dy
        if pygame.sprite.spritecollideany(self, walls):
                self.rect.y -= dy


class Maze(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    #
    # def npcmovement(self,):
    #     """This is the movement for the npc which makes it randomly use different movements
    #     to reach the player. """
    #     if self.path == "north":
    #         self.rect.move_ip(0, -self.move_distance)
    #         self.position[1] -= self.move_distance
    #     elif self.path == "south":
    #         self.rect.move_ip(0, self.move_distance)
    #         self.position[1] += self.move_distance
    #     if self.path == "east":
    #         self.rect.move_ip(self.move_distance, 0)
    #         self.position[0] -= self.move_distance
    #     if self.path == "west":
    #         self.rect.move_ip(-self.move_distance, 0)
    #         self.position[0] += self.move_distance
    #
    #     self.npc_directions()

#
# class Player(Entity):
#     """This will differinciate the player on the screen which is controllable to
#     the user compared to the npc."""
#
#
# pass
