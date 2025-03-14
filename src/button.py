class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        """Initialize a button with given position, size, text, and colors."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.hover_color = hover_color
    
    def is_clicked(self, mouse_x, mouse_y):
        """Check if the button is clicked."""
        return (self.x <= mouse_x <= self.x + self.width and 
                self.y <= mouse_y <= self.y + self.height)
                
    def draw(self, screen, font):
        """Draw the button on the screen."""
        # Import pygame here to avoid circular imports
        import pygame
        
        # Draw the button rectangle
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        
        # Draw the button text
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)