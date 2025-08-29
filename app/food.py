"""
Food class for managing food spawning and collision detection
Demonstrates DSA concepts: random sampling and set operations
"""
import random
from app.config import *

class Food:
    def __init__(self):
        self.position = None
        self.spawn()
    
    def spawn(self, snake_positions=None):
        """
        Spawn food at random position avoiding snake body
        
        DSA Concepts:
        - Set operations for O(1) lookup time
        - Random sampling from valid positions
        - List comprehension for filtering
        """
        if snake_positions is None:
            snake_positions = set()
        else:
            # Convert to set for O(1) lookup instead of O(n) list lookup
            snake_positions = set(snake_positions)
        
        # Generate all possible grid positions
        all_positions = [
            (x, y) for x in range(GRID_WIDTH) 
            for y in range(GRID_HEIGHT)
        ]
        
        # Filter out snake positions using set difference - O(n) where n is grid size
        # Alternative approach: keep trying random positions until valid
        valid_positions = [pos for pos in all_positions if pos not in snake_positions]
        
        if valid_positions:
            # Random selection from valid positions - O(1)
            self.position = random.choice(valid_positions)
        else:
            # Edge case: no valid positions (game theoretically won)
            self.position = (0, 0)
    
    def get_position(self):
        """
        Get current food position
        DSA: O(1) attribute access
        """
        return self.position
    
    def is_eaten(self, snake_head):
        """
        Check if food is eaten by snake
        DSA: O(1) tuple comparison
        """
        return self.position == snake_head