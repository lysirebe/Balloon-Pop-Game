import pytest
import sys
import os

# src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from balloon import Balloon

def test_balloon_initialisation():
    """Test if a balloon is initialised with the correct properties."""
    balloon = Balloon(100, 200, 5, (255, 0, 0))
    
    assert balloon.x == 100
    assert balloon.y == 200
    assert balloon.speed == 5
    assert balloon.color == (255, 0, 0)
    assert balloon.radius > 0
    assert balloon.popped == False

def test_balloon_movement():
    """Test if a balloon moves correctly when updated."""
    balloon = Balloon(100, 200, 5, (255, 0, 0))
    initial_y = balloon.y
    
    balloon.update()
    
    assert balloon.y == initial_y - balloon.speed
    assert balloon.x == 100  # x position should remain unchanged

def test_balloon_collision_detection():
    """Test if a balloon correctly detects when it's been clicked."""
    balloon = Balloon(100, 200, 5, (255, 0, 0))
    balloon.radius = 20
    
    # Click inside the balloon
    assert balloon.is_clicked(95, 195) == True
    
    # Click outside the balloon
    assert balloon.is_clicked(50, 50) == False