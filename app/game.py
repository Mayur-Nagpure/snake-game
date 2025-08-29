"""
Main game class handling game loop, events, and rendering
Demonstrates DSA concepts in game state management
"""
import pygame
import sys
from app.snake import Snake
from app.food import Food
from app.config import *

class Game:
    def __init__(self):
        """
        Initialize game components
        DSA: Object composition and state management
        """
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game - DSA Demo")
        self.clock = pygame.time.Clock()
        
        # Game objects
        self.snake = Snake()
        self.food = Food()
        # Spawn initial food avoiding snake body
        self.food.spawn(self.snake.get_positions())
        self.score = 0
        self.game_over = False
        
        # Font for score display
        self.font = pygame.font.Font(None, 36)
    
    def handle_events(self):
        """
        Handle pygame events
        DSA: Event queue processing
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            elif event.type == pygame.KEYDOWN:
                if event.key in KEY_MAP:
                    self.snake.change_direction(KEY_MAP[event.key])
                elif event.key == pygame.K_r and self.game_over:
                    self.restart_game()
                elif event.key == pygame.K_ESCAPE:
                    return False
        
        return True
    
    def update(self):
        """
        Update game state
        DSA Analysis:
        - Snake movement: O(1) due to deque operations
        - Collision detection: O(n) where n is snake length
        - Food spawning: O(grid_size) in worst case
        """
        if self.game_over:
            return
        
        # Move snake - O(1) due to deque
        self.snake.move()
        
        # Check collisions - O(n) for self collision
        if self.snake.check_collision():
            self.game_over = True
            return
        
        # Check food consumption - O(1)
        if self.food.is_eaten(self.snake.get_head()):
            self.snake.grow()  # O(1) - just sets flag
            self.score += 10
            
            # Spawn new food avoiding snake body - O(grid_size)
            self.food.spawn(self.snake.get_positions())
    
    def render(self):
        """
        Render game objects
        DSA: Iteration over deque for drawing
        """
        # Clear screen
        self.screen.fill(BLACK)
        
        if not self.game_over:
            # Draw snake - O(n) where n is snake length
            snake_positions = self.snake.get_positions()
            for i, segment in enumerate(snake_positions):
                x, y = segment
                rect = pygame.Rect(
                    x * GRID_SIZE, y * GRID_SIZE, 
                    GRID_SIZE, GRID_SIZE
                )
                # Different color for head (last segment)
                color = GREEN if i == len(snake_positions) - 1 else DARK_GREEN
                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, BLACK, rect, 1)  # Border
            
            # Draw food - O(1)
            food_x, food_y = self.food.get_position()
            food_rect = pygame.Rect(
                food_x * GRID_SIZE, food_y * GRID_SIZE,
                GRID_SIZE, GRID_SIZE
            )
            pygame.draw.rect(self.screen, RED, food_rect)
        
        # Draw score - O(1)
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw game over message
        if self.game_over:
            game_over_text = self.font.render("Game Over! Press R to restart or ESC to quit", True, WHITE)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(game_over_text, text_rect)
        
        pygame.display.flip()
    
    def restart_game(self):
        """
        Restart game by reinitializing objects
        DSA: Object reinitialization - O(1) for most components
        """
        self.snake = Snake()
        self.food = Food()
        # Spawn food avoiding snake body
        self.food.spawn(self.snake.get_positions())
        self.score = 0
        self.game_over = False
    
    def run(self):
        """
        Main game loop
        DSA: Game loop pattern with fixed time step
        """
        running = True
        while running:
            # Handle events - O(events_per_frame)
            running = self.handle_events()
            
            # Update game state - O(n) where n is snake length
            self.update()
            
            # Render - O(n) for drawing snake
            self.render()
            
            # Control frame rate
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()