import pygame


class Goat:
    def __init__(self, nt_game):
        self.screen = nt_game.screen
        self.game_parameters = nt_game.game_parameters
        self.screen_rect = nt_game.screen.get_rect()
        self.image = pygame.image.load('goat.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.game_parameters.goat_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.game_parameters.goat_speed
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
