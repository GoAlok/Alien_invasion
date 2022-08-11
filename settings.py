class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Scree settings
        self.screen_width = 720
        self.screen_height = 600
        self.bg_color = "#8FE3CF"
        
        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 2
        
        # Bullet settings
        self.bullet_speed = 3.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = "#3C3C3C"
        self.bullets_allowed = 5
        
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 25
        
        # Fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        
        # How quickly the alien point values increase.
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        
        # Fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        # Scoring
        self.alien_points = 50
    
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        
