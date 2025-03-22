import pygame
import sys
from game import Game

def main():
    """Main function to run the game."""
    # Initialize the game
    game = Game(800, 600)
    clock = pygame.time.Clock()
    
    # Main game loop
    running = True
    balloon_spawn_timer = 0
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                
                if game.state == "menu":
                    if game.start_button.is_clicked(mouse_x, mouse_y):
                        game.state = "play"
                    elif game.quit_button.is_clicked(mouse_x, mouse_y):
                        running = False
                
                elif game.state == "play":
                    # Check if any balloon is clicked
                    for balloon in game.balloons[:]:
                        if balloon.is_clicked(mouse_x, mouse_y):
                            balloon.popped = True
                            game.balloons.remove(balloon)
                            game.increment_score()
                
                elif game.state == "win" or game.state == "lose":
                    # Return to menu
                    game.state = "menu"
                    game.score = 0
                    game.missed_balloons = 0
                    game.balloons = []
        
        # Update game state
        if game.state == "play":
            # Spawn new balloons
            balloon_spawn_timer += 1
            if balloon_spawn_timer >= 60: 
                game.spawn_balloon()
                balloon_spawn_timer = 0
            
            # Update balloons
            for balloon in game.balloons[:]:
                balloon.update()
                
                # Check if balloon has escaped
                if balloon.y + balloon.radius < 0:
                    game.balloons.remove(balloon)
                    game.missed_balloons += 1
            
            # Check win/lose conditions
            if game.check_win():
                game.state = "win"
            elif game.check_lose():
                game.state = "lose"
        
        # Draw everything
        game.screen.fill((0, 0, 0))  # Black background
        
        if game.state == "menu":
            # Draw title
            title_text = game.font.render("Balloon Pop Game", True, (255, 255, 255))
            title_rect = title_text.get_rect(center=(game.width // 2, game.height // 4))
            game.screen.blit(title_text, title_rect)
            
            # Draw buttons
            game.start_button.draw(game.screen, game.font)
            game.quit_button.draw(game.screen, game.font)
        
        elif game.state == "play":
            # Draw score
            score_text = game.font.render(f"Score: {game.score}/{game.target_score}", True, (255, 255, 255))
            game.screen.blit(score_text, (10, 10))
            
            # Draw missed balloons
            missed_text = game.font.render(f"Missed: {game.missed_balloons}/{game.max_missed}", True, (255, 255, 255))
            game.screen.blit(missed_text, (10, 50))
            
            # Draw balloons
            for balloon in game.balloons:
                pygame.draw.circle(game.screen, balloon.color, (balloon.x, balloon.y), balloon.radius)
        
        elif game.state == "win":
            # Draw win message
            win_text = game.font.render("You Win!", True, (0, 255, 0))
            win_rect = win_text.get_rect(center=(game.width // 2, game.height // 2))
            game.screen.blit(win_text, win_rect)
            
            # Draw return to menu message
            return_text = game.font.render("Click anywhere to return to menu", True, (255, 255, 255))
            return_rect = return_text.get_rect(center=(game.width // 2, game.height // 2 + 50))
            game.screen.blit(return_text, return_rect)
        
        elif game.state == "lose":
            # Draw lose message
            lose_text = game.font.render("Game Over!", True, (255, 0, 0))
            lose_rect = lose_text.get_rect(center=(game.width // 2, game.height // 2))
            game.screen.blit(lose_text, lose_rect)
            
            # Draw return to menu message
            return_text = game.font.render("Click anywhere to return to menu", True, (255, 255, 255))
            return_rect = return_text.get_rect(center=(game.width // 2, game.height // 2 + 50))
            game.screen.blit(return_text, return_rect)
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(60)
    
    # Quit pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()