import pygame
from pygame.sprite import Sprite
import os

class Ball(Sprite):
    """A class to represent a ball object."""

    def __init__(self, catch, screen):
        """Initialize the ball, and set its starting position."""
        super(Ball, self).__init__()
        self.screen = screen
        self.catch = catch

        # Load the ball image, and set its rect attribute.
        original_image = pygame.image.load(os.path.join('images', 'ball.png'))        
        self.image = pygame.transform.rotozoom(original_image, 0, 0.4)
        self.rect = self.image.get_rect()

        # Start ball near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the ball's exact position.
        self.x = float(self.rect.x)
        
    def check_edges(self):
        """Return True if ball is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        """Move the ball right or left."""
        self.x += (self.catch.ball_speed_factor *
                        self.catch.ball_direction)
        self.rect.x = self.x

    def blitme(self):
        """Draw the ball at its current location."""
        self.screen.blit(self.image, self.rect)
