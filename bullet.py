import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
#class for ship bullets.
    def __init__(self, ai_game):
#creating bullet object at ships position.
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
#creating bullet at (0,0) then correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
#store bullet position as decimal value.
        self.y = float(self.rect.y)
    def update(self):
# move bullet up the screen.
        self.y -= self.settings.bullet_speed
#updating rect pos.
        self.rect.y = self.y
    def draw_bullet(self):
#drawing the bullet on the screen.
        pygame.draw.rect(self.screen, self.color, self.rect)
        