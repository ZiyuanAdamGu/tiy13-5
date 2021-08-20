import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from character import Character
import game_functions as gf



def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Catch Game")
    
    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    
    # Set the background color.
    bg_color = (230, 230, 230)
    
    # Make a character, and a ball.
    character = Character(ai_settings, screen)
    ball = Group()

    # Background sprites

    # Start the main loop for the game.
    while True:
        gf.check_events(catch, screen, character, ball)
        
        if stats.game_active:
            character.update()
            gf.update_ball(ai_settings, stats, screen, character, ball)
        
        gf.update_screen(ai_settings, screen, character, ball, None)

run_game()