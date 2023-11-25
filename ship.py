import pygame
pygame.init()
class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        original_image = pygame.image.load("images/grinch.png")
        scaled_width = int(original_image.get_width() * 0.0625)
        scaled_height = int(original_image.get_height() * 0.0625)
        self.image = pygame.transform.scale(original_image, (scaled_width, scaled_height))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        #Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        #Movement flag
        self.moving_right = False
        self.moving_left = False
    def update(self):
        #update the ship's position based on the movement flag.
        #update ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #update rect object from self.x.
        self.rect.x = self.x
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def center_ship(self):
        #center the ship on the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)