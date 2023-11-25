import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #rep an alien
    def __init__(self, ai_game):
    #initialize the alien
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
    #alien image and rect attribute
        alien_image = pygame.image.load("images/christmas_tree.png")
    #Image was too big. Had to scale the image down to size
        scale_width = int(alien_image.get_width() * 0.0625)
        scale_height = int(alien_image.get_height() * 0.0625)
        self.image = pygame.transform.scale(alien_image, (scale_width, scale_height))
        self.rect = self.image.get_rect()
        self.rect.topleft =self.screen_rect.topleft
    def check_edges(self):
    #return true if alien is at edge of screen.
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    def update(self):
    #move alien right or left.
        self.x += (self.settings.alien_speed *
                    self.settings.fleet_direction)
        self.rect.x = self.x
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    