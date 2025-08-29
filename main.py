#!/usr/bin/env python3
"""
Snake Game - Entry Point
Demonstrates Data Structures and Algorithms using collections.deque

DSA Concepts Demonstrated:
1. Deque: O(1) append/pop operations for snake movement
2. Set operations: O(1) lookup for collision detection optimization
3. Random sampling: Efficient food placement
4. List comprehension: Functional programming for position filtering
5. Event-driven programming: Queue-based event handling

"""
import sys
import os

# Add the project root to Python path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.game import Game

def main():
    
    try:
        print("🐍 Starting Snake Game with DSA Demo...")
        print("Controls:")
        print("  Arrow Keys or WASD: Move snake")
        print("  R: Restart game (when game over)")
        print("  ESC: Quit game")
        print("\nDSA Features:")
        print("  - collections.deque for O(1) snake body management")
        print("  - Set operations for efficient collision detection")
        print("  - Random sampling for food placement")
        print("\nStarting game...")
        
        game = Game()
        game.run()
        
    except KeyboardInterrupt:
        print("\n🛑 Game interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error running game: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()