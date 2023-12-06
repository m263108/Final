import pygame
from pygame import mixer
from pygame.locals import *
class Game_parameters:
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0, 0, 165)
        self.football_width = 40
        self.football_height = 40
        self.footballs_allowed = 5
        self.fleet_drop_speed = 20
        self.goat_limit = 3
        self.speedup_scale = 1.35
        self.score_scale = 2
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        self.goat_speed = .75
        self.football_speed = 1
        self.mule_speed = .5
        self.fleet_direction = 1
        self.mule_points = 50

    def increase_speed(self):
        self.goat_speed *= self.speedup_scale
        self.football_speed *= self.speedup_scale
        self.mule_speed *= self.speedup_scale
        self.mule_points = int(self.mule_points * self.score_scale)


