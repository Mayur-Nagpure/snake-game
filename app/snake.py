"""
Snake class implementation using collections.deque
Demonstrates DSA concepts: deque for O(1) head/tail operations
"""
from collections import deque
from app.config import *

class Snake:
    def __init__(self, start_pos=None):
        """
        Initialize snake using deque data structure
        
        Why deque?
        - O(1) append and appendleft operations for adding new head
        - O(1) pop and popleft operations for removing tail
        - Better than list for frequent insertions/deletions at both ends
        - In Snake game: constant head additions and tail removals
        """
        self.body = deque()
        self.direction = RIGHT
        self.grow_next = False
        
        # Set default starting position
        if start_pos is None:
            start_pos = (GRID_WIDTH // 2, GRID_HEIGHT // 2)
        
        # Initialize snake body with starting positions
        # Create initial snake body moving left to right
        for i in range(INITIAL_SNAKE_LENGTH):
            x = start_pos[0] - (INITIAL_SNAKE_LENGTH - 1 - i)
            y = start_pos[1]
            # Ensure we don't go out of bounds
            x = max(0, min(x, GRID_WIDTH - 1))
            self.body.append((x, y))
    
    def move(self):
        """
        Move snake in current direction
        DSA Efficiency:
        - append(): O(1) - add new head to right end
        - popleft(): O(1) - remove tail from left end
        - Total: O(1) time complexity for movement
        """
        # Get current head position (rightmost element)
        head_x, head_y = self.body[-1]  # O(1) access to head
        
        # Calculate new head position
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        
        # Add new head to right end of deque - O(1)
        self.body.append(new_head)
        
        # Remove tail if not growing - O(1)
        if not self.grow_next:
            self.body.popleft()  # Remove from left end (tail)
        else:
            self.grow_next = False
    
    def grow(self):
        """
        Mark snake to grow on next move
        Growth is handled in move() method by not removing tail
        """
        self.grow_next = True
    
    def change_direction(self, new_direction):
        """
        Change snake direction with validation
        Prevents 180-degree turns that would cause immediate collision
        """
        # Prevent reverse direction (DSA logic: opposite vector check)
        opposite_directions = {
            UP: DOWN,
            DOWN: UP,
            LEFT: RIGHT,
            RIGHT: LEFT
        }
        
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction
    
    def check_collision(self):
        """
        Check for collisions using deque properties
        
        DSA Analysis:
        - Wall collision: O(1) - simple coordinate check
        - Self collision: O(n) where n is snake length
        - Using 'in' operator on deque: O(n) but necessary for game logic
        """
        # Check if we have any body segments
        if len(self.body) == 0:
            return True
            
        head_x, head_y = self.body[-1]  # O(1) head access (rightmost)
        
        # Check wall collision - O(1)
        if (head_x < 0 or head_x >= GRID_WIDTH or 
            head_y < 0 or head_y >= GRID_HEIGHT):
            return True
        
        # Check self collision - O(n)
        # Check if head position exists in body (excluding the head itself)
        body_without_head = list(self.body)[:-1]  # All except last (head)
        return self.body[-1] in body_without_head
    
    def get_positions(self):
        """
        Return all body positions
        DSA: O(1) access to deque as iterable
        """
        return list(self.body)
    
    def get_head(self):
        """
        Get head position
        DSA: O(1) access to right end of deque
        """
        return self.body[-1]  # Head is now at the right end