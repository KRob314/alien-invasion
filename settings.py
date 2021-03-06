class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self, shipImg):
        """Initialize the game's static settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.shipImage = shipImg


        if self.shipImage == "1":
            self.bullet_width = 15
            self.bullet_height = 15
            self.bullet_color = 60, 60, 60
            self.bullets_allowed = 1
            self.fleet_drop_speed = 15
            self.ship_limit = 2
            self.speedup_scale = .9    
            self.score_scale = 1.5 
        if self.shipImage == "2":          
            # Bullet settings.
            self.bullet_width = 8
            self.bullet_height = 15
            self.bullet_color = 60, 60, 60
            self.bullets_allowed = 3
            self.fleet_drop_speed = 10
            self.ship_limit = 4
            self.speedup_scale = 1.1      
            self.score_scale = 1.5 
        else:
            self.bullet_width = 3
            self.bullet_height = 15
            self.bullet_color = 60, 60, 60
            self.bullets_allowed = 5
            self.fleet_drop_speed = 20
            self.ship_limit = 5
            self.speedup_scale = 1.3     
            self.score_scale = 1.5                          
    
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        #print("dynamic_settings ")
        #print( self.shipImage)
        if self.shipImage == "1":
            self.ship_speed_factor = 1
            self.bullet_speed_factor = 3
            self.alien_speed_factor = .5
            self.alien_points = 50
        if self.shipImage == "2":
            self.ship_speed_factor = 1.5
            self.bullet_speed_factor = 5
            self.alien_speed_factor = 1
            self.alien_points = 75
        else:
            self.ship_speed_factor = 2.5
            self.bullet_speed_factor = 10
            self.alien_speed_factor = 1.1
            self.alien_points = 100
        
        # Scoring.
        #self.alien_points = 50
    
        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1
        
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
