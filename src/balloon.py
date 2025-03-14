import math
import random

class Balloon:
    def __init__(self, x, y, speed, color):
        """Initialise a balloon with given position, speed, and color."""
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.radius = random.randint(20, 40)
        self.popped = False
    
    def update(self):
        """Update the balloon's position."""
        if not self.popped:
            self.y -= self.speed
    
    def is_clicked(self, mouse_x, mouse_y):
        """Check if the balloon is clicked."""
        if self.popped:
            return False
            
        # Calculate distance between mouse position and balloon center
        distance = math.sqrt((mouse_x - self.x) ** 2 + (mouse_y - self.y) ** 2)
        
        # If distance is less than radius, balloon is clicked
        return distance <= self.radius
    
    