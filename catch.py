import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from character import Character
import game_functions as gf



def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    catch = Settings()
    screen = pygame.display.set_mode(
        (catch.screen_width, catch.screen_height))
    pygame.display.set_caption("Catch Game")
    
    # Create an instance to store game statistics.
    stats = GameStats(catch)
    
    # Set the background color.
    bg_color = (230, 230, 230)
    
    # Make a character, and a ball.
    character = Character(catch, screen)
    ball = Group()

    # Background sprites

    # Start the main loop for the game.
    while True:
        gf.check_events(screen, character, ball)
        
        if stats.game_active:
            character.update()
            gf.update_ball(catch, stats, screen, character, ball)
        
        gf.update_screen(screen, character, ball, None)

run_game()