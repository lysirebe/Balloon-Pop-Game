import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from button import Button

def test_button_initialization():
    """Test if a button is initialized with the correct properties."""
    button = Button(100, 150, 200, 50, "Start", (255, 0, 0), (0, 255, 0))
    
    assert button.x == 100
    assert button.y == 150
    assert button.width == 200
    assert button.height == 50
    assert button.text == "Start"
    assert button.color == (255, 0, 0)
    assert button.hover_color == (0, 255, 0)

def test_button_click_detection():
    """Test if a button correctly detects when it's been clicked."""
    button = Button(100, 150, 200, 50, "Start", (255, 0, 0), (0, 255, 0))
    
    # Click inside the button
    assert button.is_clicked(150, 175) == True
    
    # Click outside the button
    assert button.is_clicked(50, 50) == False