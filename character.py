import pygame
import os

class Character():

    def __init__(self, catch, screen):
        """Initialize the character, and set its starting position."""
        self.screen = screen
        self.catch = catch
        """Create self.fill to colour screen."""
        self.fill = fill
        # Load the character image, and get its rect.
        original_image = pygame.image.load(os.path.join('character.png'))
        self.image = pygame.transform.rotozoom(original_image, 0, 0.15)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new character at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Store a decimal value for the character's center.
        self.center = float(self.rect.centerx)
        
        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        
    def center_character(self):
        """Center the character on the screen."""
        self.center = self.screen_rect.centerx
        
    def update(self):
        """Update the character's position, based on movement flags."""
        # Update the character's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.catch.character_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.catch.character_speed_factor
            
        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)
