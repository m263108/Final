class Score:
    def __init__(self,nt_game):
        self.game_parameters= nt_game.game_parameters
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
    def reset_stats(self):
        self.goats_left = self.game_parameters.goat_limit
        self.score = 0

