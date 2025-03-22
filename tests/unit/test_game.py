import pytest
import sys
import os
import pygame

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from game import Game

# Initialize pygame for testing
pygame.init()

def test_game_initialisation():
    """Test if the game is initialized with the correct properties."""
    game = Game(800, 600)
    
    assert game.width == 800
    assert game.height == 600
    assert game.score == 0
    assert game.state == "menu"
    assert len(game.balloons) == 0
    assert game.missed_balloons == 0
    assert game.target_score > 0
    assert game.max_missed > 0

def test_game_score_increment():
    """Test if the game score increments correctly."""
    game = Game(800, 600)
    initial_score = game.score
    
    game.increment_score()
    
    assert game.score == initial_score + 1

def test_win_condition():
    """Test if the game correctly detects the win condition."""
    game = Game(800, 600)
    game.target_score = 10
    game.score = 9
    
    assert game.check_win() == False
    
    game.score = 10
    
    assert game.check_win() == True

