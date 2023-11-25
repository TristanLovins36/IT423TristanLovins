class GameStats:
#Tract statustics for ALien Invasion
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
#start alien invasion in an active state.
        self.game_active = True
    def reset_stats(self):
#initialize stats that change
        self.ships_left = self.settings.ship_limit
