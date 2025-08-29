"""
Configuration file for Snake Game
Contains all game constants and settings
"""
import pygame

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors (RGB)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
DARK_GREEN = (0, 155, 0)

# Game settings
FPS = 10
INITIAL_SNAKE_LENGTH = 3

# Directions (using tuples for immutability - good DSA practice)
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Key mappings
KEY_MAP = {
    pygame.K_UP: UP,
    pygame.K_DOWN: DOWN,
    pygame.K_LEFT: LEFT,
    pygame.K_RIGHT: RIGHT,
    pygame.K_w: UP,
    pygame.K_s: DOWN,
    pygame.K_a: LEFT,
    pygame.K_d: RIGHT
}