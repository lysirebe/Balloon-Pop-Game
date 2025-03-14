import pygame
import random
from balloon import Balloon
from button import Button

class Game:
    def __init__(self, width, height):
        """Initialize the game with given dimensions."""
        self.width = width
        self.height = height
        self.score = 0
        self.state = "menu"  # "menu", "play", "win", "lose"
        self.balloons = []
        self.missed_balloons = 0
        self.target_score = 20
        self.max_missed = 10
        
        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Balloon Pop Game")
        self.font = pygame.font.Font(None, 36)
        
        # Create buttons
        self.start_button = Button(width // 2 - 100, height // 2 - 25, 200, 50, "Play", (0, 128, 0), (0, 196, 0))
        self.quit_button = Button(width // 2 - 100, height // 2 + 50, 200, 50, "Quit", (196, 0, 0), (255, 0, 0))
    
    def increment_score(self):
        """Increment the game score."""
        self.score += 1
    
    def check_win(self):
        """Check if the player has won."""
        return self.score >= self.target_score
    
    def check_lose(self):
        """Check if the player has lost."""
        return self.missed_balloons >= self.max_missed
    
    def spawn_balloon(self):
        """Spawn a new balloon at a random position."""
        x = random.randint(50, self.width - 50)
        y = self.height + 50
        speed = random.randint(1, 4)
        
        # Random color
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
        color = random.choice(colors)
        
        self.balloons.append(Balloon(x, y, speed, color))