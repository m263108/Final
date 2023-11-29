import sys
import pygame
from game_parameters import Game_parameters
from goat import Goat
from football import Football
from mule import Mule


class NavyTakeover:
    def __init__(self):
        pygame.init()
        self.game_parameters = Game_parameters()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.game_parameters.screen_width = self.screen.get_rect().width
        self.game_parameters.screen_height = self.screen.get_rect().height
        # self.screen=pygame.display.set_mode((self.game_parameters.screen_width, self.game_parameters.screen_height))
        pygame.display.set_caption("Navy Takeover")
        self.bg_color = (0, 0, 165)
        self.goat = Goat(self)
        self.footballs = pygame.sprite.Group()
        self.mules = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.goat.update()
            self._update_footballs()
            self._update_mules()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.goat.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.goat.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._throw_football()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.goat.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.goat.moving_left = False

    def _create_fleet(self):
        mule = Mule(self)
        mule_width, mule_height = mule.rect.size
        available_space_x = self.game_parameters.screen_width - (2 * mule_width)
        number_mules_x = available_space_x // (2 * mule_width)
        goat_height = self.goat.rect.height
        available_space_y = (self.game_parameters.screen_height - (3 * mule_height) - goat_height)
        number_rows = available_space_y // (2 * mule_height)
        for row_number in range(number_rows):
            for mule_number in range(number_mules_x):
                self._create_mule(mule_number, row_number)

    def _create_mule(self, mule_number, row_number):
        mule = Mule(self)
        mule_width, alien_height = mule.rect.size
        mule.x = mule_width + 2 * mule_width * mule_number
        mule.rect.x = mule.x
        mule.rect.y = mule.rect.height + 2 * mule.rect.height * row_number
        self.mules.add(mule)

    def _check_fleet_edges(self):
        for mule in self.mules.sprites():
            if mule.check_edges() and mule.rect.right >= self.screen.get_rect().right:
                self._change_fleet_direction()
                self.game_parameters.fleet_direction = -1
            if mule.check_edges() and mule.rect.x <= 0:
                self.game_parameters.fleet_direction = 1
                # self._change_fleet_direction()
                # break

    def _change_fleet_direction(self):
        for mule in self.mules.sprites():
            mule.rect.y += self.game_parameters.fleet_drop_speed
            # if self.game_parameters.fleet_direction == 1:
            #     self.game_parameters.fleet_direction = 1
            # else:
            # print(self.game_parameters.fleet_direction)

            self.game_parameters.fleet_direction = -1

    def _throw_football(self):
        new_football = Football(self)
        self.footballs.add(new_football)

    def _update_footballs(self):
        self.footballs.update()
        for football in self.footballs.copy():
            if football.rect.bottom <= 0:
                self.footballs.remove(football)
        collisions = pygame.sprite.groupcollide(self.footballs, self.mules, True, True)

    def _update_mules(self):
        self._check_fleet_edges()
        self.mules.update()

    def _update_screen(self):
        self.screen.fill(self.game_parameters.bg_color)
        self.goat.blitme()
        for football in self.footballs.sprites():
            football.blitme()
        self.mules.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    nt = NavyTakeover()
    nt.run_game()
