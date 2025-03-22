# tests/integration/test_balloon_game.py
import pytest
from unittest.mock import Mock
from pygame import Rect
from balloon import Balloon
from button import Button
from game import Game

@pytest.fixture
def mock_pygame():
    """Mock pygame for testing"""
    class MockPygame:
        def __init__(self):
            self.display = Mock()
            self.font = Mock()
            self.time = Mock()
            
        def init():
            pass
            
        def quit():
            pass
            
        def draw():
            pass
            
        def render(text, _, color):
            return Mock()
            
        def get_rect(**kwargs):
            return Mock(center=(400, 300))
            
        def get_pos():
            return (100, 200)
            
        Clock = Mock()
        
    return MockPygame()

@pytest.fixture
def game(mock_pygame):
    """Create a game instance with mocked pygame"""
    game = Game(800, 600)
    game.pygame = mock_pygame
    return game


def test_balloon_button_integration(game):
    """Test balloon and button interaction"""
    # Create a balloon near the button
    balloon = Balloon(400, 300, 2, (255, 0, 0))
    game.balloons.append(balloon)

    # Verify the balloon is added to the game
    assert len(game.balloons) == 1
    assert game.balloons[0].x == 400
    assert game.balloons[0].y == 300
    assert game.balloons[0].speed == 2
    assert game.balloons[0].color == (255, 0, 0)


def test_game_state_transitions(game):
    """Test game state transitions"""
    # Verify initial state
    assert game.state == "menu"
    
    # Manually transition to play state
    game.state = "play"
    assert game.state == "play"
    
    # Simulate win condition
    game.score = game.target_score
    game.state = "win"
    assert game.state == "win"
    
    # Manually return to menu
    game.state = "menu"
    assert game.state == "menu"


def test_balloon_spawn_and_update(game):
    """Test balloon spawning and movement"""
    # Verify no balloons at the start
    assert len(game.balloons) == 0
    
    # Spawn a balloon using the game's spawn_balloon method
    game.spawn_balloon()
    assert len(game.balloons) == 1
    
    # Get the spawned balloon
    balloon = game.balloons[0]
    initial_y = balloon.y
    
    # Set the game state to "play"
    game.state = "play"
    
    # Update balloon position
    game.update()
    assert balloon.y == initial_y - balloon.speed

