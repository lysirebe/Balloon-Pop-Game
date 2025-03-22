import pytest
import pygame
import sys
import time
from unittest.mock import Mock, patch
sys.path.insert(0, './src')
from game import Game
from balloon import Balloon
from button import Button

class TestBalloonPopAcceptance:
    @pytest.fixture
    def setup_pygame(self):
        pygame.init()
        yield
        pygame.quit()
    
    @pytest.fixture
    def game(self, setup_pygame):
        game = Game(800, 600)
        return game
    
    def test_menu_screen_implementation(self, game):
        """ Test that the menu screen displays with functional buttons"""
        # Verify game starts in menu state
        assert game.state == "menu"

        # Verify the start and quit buttons exist
        assert game.start_button is not None
        assert game.quit_button is not None

        # Test start button functionality
        mock_event = Mock()
        mock_event.type = pygame.MOUSEBUTTONDOWN

        # Corrected code
        button_x = game.start_button.x + game.start_button.width // 2  
        button_y = game.start_button.y + game.start_button.height // 2


        # Debug print statements
        print(f"Start button position: ({game.start_button.x}, {game.start_button.y})")
        print(f"Start button dimensions: {game.start_button.width}x{game.start_button.height}")
        print(f"Simulated click position: ({button_x}, {button_y})")


        with patch('pygame.mouse.get_pos', return_value=(button_x, button_y)):
            with patch('pygame.event.get', return_value=[mock_event]):
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        if game.start_button.is_clicked(mouse_x, mouse_y):
                            game.state = "play"

        assert game.state == "play", "Clicking the start button should change state to play"

        # Reset game state for quit button test
        game.state = "menu"

        # Test quit button functionality
        should_quit = False

        # Simulate clicking the quit button
        button_x = game.quit_button.x + game.quit_button.width // 2
        button_y = game.quit_button.y + game.quit_button.height // 2

        with patch('pygame.mouse.get_pos', return_value=(button_x, button_y)):
            with patch('pygame.event.get', return_value=[mock_event]):
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        if game.quit_button.is_clicked(mouse_x, mouse_y):
                            should_quit = True

        # Verify clicking quit button would exit game
        assert should_quit == True, "Clicking the quit button should exit the game"
    
    def test_at003_win_lose_scenarios(self, game):
        """
        Test that the game displays appropriate messages for win and lose conditions
        """
        # Test win scenario
        game.state = "play"
        game.score = game.target_score
        
        if game.score > game.target_score:
            game.state = "win"
        
        assert game.state == "win" 
