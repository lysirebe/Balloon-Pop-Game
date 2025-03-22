# tests/regression/test_game_behavior.py
import pytest
from unittest.mock import Mock
from game import Game

@pytest.fixture
def game():
    """Create a game instance for regression testing"""
    return Game(800, 600)

def test_win_condition_regression(game):
    """Verify win condition behavior"""
    # Save initial target score
    initial_target = game.target_score
    
    # Test winning with exact score
    game.score = initial_target
    assert game.check_win()
    
    # Test winning with higher score
    game.score += 1
    assert game.check_win()
    
    # Test not winning with lower score
    game.score = initial_target - 1
    assert not game.check_win()

def test_balloon_spawn_regression(game):
    """Verify balloon spawning behavior"""
    # Save initial spawn parameters
    initial_width = game.width
    initial_height = game.height
    
    # Spawn balloons and verify positions
    for _ in range(10):
        game.spawn_balloon()
        balloon = game.balloons[-1]
        
        # Verify x position within bounds
        assert 50 <= balloon.x <= initial_width - 50
        
        # Verify y position at bottom
        assert balloon.y == initial_height + 50
        
        # Verify speed within expected range
        assert 1 <= balloon.speed <= 4
        
        # Remove balloon for next iteration
        game.balloons.pop()

@pytest.mark.parametrize("score,expected_state", [
    (19, "play"),
    (20, "win"),
    (21, "win")
])
def test_score_transitions_regression(game, score, expected_state):
    """Test score transitions"""
    game.state = "play"  # Ensure the game starts in the "play" state
    game.score = score
    game.update()
    assert game.state == expected_state
