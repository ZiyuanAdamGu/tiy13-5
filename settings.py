class Settings():
    """A class to store all settings for Catch Game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.        
        self.screen_width = 450
        self.screen_height = 300
        self.bg_color = (6,57,112)
        
        # Character settings.
        self.character_speed_factor = 1.5
        self.character_limit = 3

        # Ball settings.
        self.ball_speed_factor = 0.25