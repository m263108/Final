import pygame
from pygame.sprite import Sprite


class Football(Sprite):
    def __init__(self, nt_game):
        super().__init__()
        self.screen = nt_game.screen
        self.game_parameters = nt_game.game_parameters
        self.image = pygame.image.load('football.png')
        self.rect = pygame.Rect(0, 0, self.game_parameters.football_width, self.game_parameters.football_height)
        self.rect.midtop = nt_game.goat.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.game_parameters.football_speed
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
