import sys
from time import sleep

import pygame
from ball import Ball


def check_keydown_events(event, ai_settings, screen, character):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        character.moving_right = True
    elif event.key == pygame.K_LEFT:
        character.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
        
def check_keyup_events(event, character):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        character.moving_right = False
    elif event.key == pygame.K_LEFT:
        character.moving_left = False

def check_events(ai_settings, screen, character):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, character)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event)
            

def update_screen(ai_settings, screen, character, balls):
    """Update images on the screen, and flip to the new screen."""
    # Redraw the screen, each pass through the loop.
    screen.fill(ai_settings.bg_color)
        
    
def character_hit(ai_settings, stats, screen, character, balls):
    """Respond to character being hit by ball. Game over."""
    if stats.characters_left > 0:
        # Decrement characters_left.
        stats.characters_left -= 1
    else:
        stats.game_active = False
    
    # Empty the list of balls.
    balls.empty()
    
    # Pause.
    sleep(0.5)
    
def check_balls_bottom(ai_settings, stats, screen, character, balls):
    """Check if any balls have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for ball in balls.sprites():
        if ball.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the character got hit.
            character_hit(ai_settings, stats, screen, character, balls)
            break
          
def update_ball(ai_settings, stats, screen, character, balls, bullets):
    
    # Look for ball-character collisions.
    if pygame.sprite.spritecollideany(character, balls):
        character_hit(ai_settings, stats, screen, character, balls, bullets)

    # Look for balls hitting the bottom of the screen.
    check_balls_bottom(ai_settings, stats, screen, character, balls, bullets)
            
    
def create_ball(ai_settings, screen, balls):
    """Create an ball;"""
    ball = Ball(ai_settings, screen)
    ball_width = ball.rect.width
    ball.x = ball_width + 2 * ball_width * ball_number
    ball.rect.x = ball.x
    ball.rect.y = ball.rect.height + 2 * ball.rect.height * row_number
    balls.add(ball)


