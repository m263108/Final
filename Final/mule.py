import pygame
from pygame.sprite import Sprite


class Mule(Sprite):
    def __init__(self, nt_game):
        super().__init__()
        self.screen = nt_game.screen
        self.game_parameters = nt_game.game_parameters
        self.image = pygame.image.load('mule.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True

    def update(self):
        # print(self.game_parameters.fleet_direction)
        self.x += (self.game_parameters.mule_speed * self.game_parameters.fleet_direction)
        self.rect.x = self.x
