# 🏓 Enhanced Pong Game

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Turtle Graphics](https://img.shields.io/badge/Graphics-Turtle-green.svg)](https://docs.python.org/3/library/turtle.html)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Game Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](https://github.com/qusai-Kagalwala/enhanced-pong-game)

> 🎮 A modern take on the classic Pong game with professional enhancements and polished gameplay experience

## 🌟 Features

### ✨ Game Enhancements
- 🏆 **Win Conditions** - First player to reach 5 points wins
- 🎯 **Professional Court Design** - Dotted center line divider
- 🚀 **Progressive Difficulty** - Ball speed increases after each paddle hit
- 🛡️ **Boundary Protection** - Paddles can't move off-screen
- 🎨 **Winner Celebration** - Trophy emojis and coloured victory message

### 🔧 Technical Improvements
- 📦 **Modular Architecture** - Clean separation of concerns
- 🎯 **Improved Collision Detection** - Rectangular boundaries instead of circular
- ⚡ **Performance Optimised** - Smooth 60fps gameplay
- 📋 **Organised Constants** - No magic numbers, easy customisation
- 📚 **Comprehensive Documentation** - Detailed code comments

## 🎮 How to Play

### 🕹️ Controls
| Player | Up | Down |
|--------|----|----|
| **Left Player** | `W` | `S` |
| **Right Player** | `↑` | `↓` |

### 🏆 Objective
- Prevent the ball from reaching your side of the court
- First player to score **5 points** wins the match
- Ball speed increases with each paddle hit for added challenge

## 🚀 Quick Start

### 📋 Prerequisites
- Python 3.6 or higher
- Turtle graphics module (included with Python)

### ⚡ Installation & Run
```bash
# Clone the repository
git clone https://github.com/qusai-Kagalwala/enhanced-pong-game.git

# Navigate to project directory
cd enhanced-pong-game

# Run the game
python main.py
```

## 📁 Project Structure

```
enhanced-pong-game/
├── 📄 main.py          # Main game loop and setup
├── 🏓 paddle.py        # Paddle class with boundary checking
├── ⚽ ball.py           # Ball physics and movement
├── 📊 scoreboard.py    # Score tracking and winner display
├── ➖ center_line.py   # Professional court center line
└── 📖 README.md        # Project documentation
```

## 🎯 Game Components

### 🏓 Paddle System
- **Boundary Checking**: Prevents paddles from leaving the screen
- **Smooth Movement**: 20-pixel increments for responsive control
- **Position Tracking**: Accurate collision detection boundaries

### ⚽ Ball Physics
- **Realistic Bouncing**: Off walls and paddles
- **Speed Progression**: Gets faster after each paddle hit
- **Reset Mechanism**: Returns to center after each point

### 📊 Scoreboard
- **Real-time Updates**: Instant score display
- **Winner Announcement**: Trophy celebration with yellow highlighting
- **Professional Fonts**: Clean, readable score display

### ➖ Court Design
- **Dotted Center Line**: Professional tennis court appearance
- **Clean Boundaries**: Clear visual separation between player sides

## 🔧 Customisation Options

### 🎨 Game Settings (in `main.py`)
```python
# Screen Configuration
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINNING_SCORE = 5  # Change winning score

# Paddle Configuration  
PADDLE_SPEED = 20  # Adjust paddle movement speed

# Ball Configuration
INITIAL_MOVE_DISTANCE = 10  # Ball movement speed
```

### 🎮 Controls (in `main.py`)
```python
# Modify control keys
RIGHT_PADDLE_UP = "Up"      # Change to any key
RIGHT_PADDLE_DOWN = "Down"
LEFT_PADDLE_UP = "w"
LEFT_PADDLE_DOWN = "s"
```

## 🏗️ Technical Details

### 🔄 Enhancement Philosophy
This project started with Angela Yu's 100 Days of Code Pong tutorial and evolved into a professional-grade game while maintaining the educational foundation:

- ✅ **Preserved Core Logic**: All original game mechanics maintained
- ✅ **Added Professional Features**: Win conditions, boundary checking, court design
- ✅ **Improved Performance**: Better collision detection and smooth animation
- ✅ **Enhanced Code Quality**: Modular structure, constants, documentation

### 🚀 Performance Features
- **Rectangular Collision Detection**: More accurate than circular distance-based detection
- **Optimised Rendering**: Turtle tracer disabled for smooth animation
- **Memory Efficient**: Proper object lifecycle management

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🌟 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit your changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to the branch (`git push origin feature/amazing-feature`)
5. 🔀 Open a Pull Request

### 💡 Contribution Ideas
- 🎵 Sound effects and background music
- 🎨 Custom themes and colour schemes  
- 🤖 AI opponent with difficulty levels
- 🏆 Tournament mode with multiple rounds
- 📊 Statistics tracking and high scores

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- 👩‍🏫 **Angela Yu** - Original Pong tutorial from 100 Days of Code
- 🐍 **Python Community** - For the amazing Turtle graphics module
- 🎮 **Classic Pong** - The timeless game that started it all

## 📞 Contact

**Qusai Kagalwala**
- 📧 Email: qusai.kagalwala53@gmail.com
- 💼 LinkedIn: [qusai-kagalwala](https://www.linkedin.com/in/qusai-kagalwala/)
- 🐙 GitHub: [@qusai-Kagalwala](https://github.com/qusai-Kagalwala)

---

<div align="center">

### 🎮 Ready to Play? Let's Pong! 🏓

**[⬆️ Back to Top](#-enhanced-pong-game)**

</div>
