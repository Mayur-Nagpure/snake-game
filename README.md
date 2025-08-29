# 🐍 Snake Game - DSA Demonstration

A fully functional Snake Game built in Python using pygame and collections.deque, showcasing practical applications of Data Structures and Algorithms in game development.

## 🎯 DSA Concepts 

### 1. **Collections.deque** - Double-ended Queue
- **Use Case**: Snake body management
- **Efficiency**: O(1) append/pop operations at both ends
- **Why not List?**: Lists have O(n) insertion at the beginning
- **Implementation**: Head additions and tail removals in constant time

### 2. **Set Operations**
- **Use Case**: Collision detection optimization
- **Efficiency**: O(1) average lookup time vs O(n) for lists
- **Implementation**: Converting snake positions to set for fast collision checks

### 3. **Random Sampling**
- **Use Case**: Food placement algorithm
- **Implementation**: Efficient selection from valid grid positions

### 4. **Event-Driven Programming**
- **Use Case**: Game input handling
- **Implementation**: Queue-based event processing with pygame

## 🚀 Quick Start

### Local Installation

1. **Clone/Download** the project
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt