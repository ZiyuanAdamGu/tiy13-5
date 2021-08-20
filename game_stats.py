class GameStats():
    """Track statistics for Catch."""
    
    def __init__(self, catch):
        """Initialize statistics."""
        self.catch = catch
        self.reset_stats()
        
        # Start Catch in an active state.
        self.game_active = True
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.characters_left = self.catch.character_limit
