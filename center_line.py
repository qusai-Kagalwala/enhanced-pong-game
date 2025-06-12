# =============================================================================
# Angela Yu's 100 Days of Code Challenge - Day 22: Center Line Class
# COMPLETELY NEW ADDITION - Creates dotted center line dividing court sides
# This class was NOT in the original Angela Yu implementation
# =============================================================================

from turtle import Turtle

# =============================================================================
# CENTER LINE CONSTANTS (NEW: All constants for the dotted line)
# =============================================================================
LINE_COLOR = "white"
DOT_SIZE = 20
DOT_SPACING = 40
SCREEN_HEIGHT = 600
LINE_POSITION_X = 0


class CenterLine(Turtle):
    """
    COMPLETELY NEW CLASS - Not in original Angela Yu code

    Center Line class that draws a dotted line down the middle of the screen
    Adds professional tennis/pong court appearance to the game
    Inherits from Turtle class for drawing capabilities

    WHY ADDED:
    - Professional sports games have court dividers
    - Visual separation between player sides
    - Makes the game look more polished and complete
    - Follows real pong/tennis court design
    """

    def __init__(self):
        """
        Initialize the center line turtle
        NEW FUNCTIONALITY: Sets up turtle for drawing dotted pattern
        """
        super().__init__()
        self.color(LINE_COLOR)
        self.penup()  # Start with pen up
        self.hideturtle()  # Hide the turtle cursor
        self.speed("fastest")  # Draw as fast as possible

    def draw(self):
        """
        NEW METHOD: Draw the dotted center line from top to bottom of screen
        Creates alternating pattern of dots and gaps

        TECHNIQUE USED:
        - Move turtle to top center of screen
        - Draw dot (pen down, move forward, pen up)
        - Create gap (pen up, move forward)
        - Repeat until bottom of screen reached
        """
        # Start from top of screen
        start_y = SCREEN_HEIGHT // 2
        end_y = -(SCREEN_HEIGHT // 2)

        # Move to starting position (top center)
        self.goto(LINE_POSITION_X, start_y)
        self.setheading(270)  # Point downward (270 degrees)

        # Draw dotted line pattern using alternating pen down/up
        current_y = start_y
        while current_y > end_y:
            # Draw a dot (pen down and move)
            self.pendown()
            self.forward(DOT_SIZE)
            current_y -= DOT_SIZE

            # Create gap (pen up and move)
            self.penup()
            self.forward(DOT_SPACING)
            current_y -= DOT_SPACING

# =============================================================================
# WHY THIS CLASS WAS ADDED TO ANGELA YU'S ORIGINAL CODE:
#
# ORIGINAL ANGELA YU PONG (Day 22):
# - Black screen with white paddles and ball
# - Simple, functional game
# - No visual court elements
# - Focus on core game mechanics
#
# ENHANCEMENT REASONING:
# 1. 🎾 REALISM: Real pong/tennis courts have center dividers
# 2. 👁️ VISUAL APPEAL: Makes the game look more professional
# 3. 🎮 USER EXPERIENCE: Clear visual separation between player sides
# 4. 🏆 POLISH: Adds that "finished game" feel
# 5. 📚 LEARNING: Demonstrates turtle graphics drawing techniques
#
# TECHNICAL IMPLEMENTATION:
# - Uses turtle's penup()/pendown() for dotted pattern
# - Calculates screen boundaries automatically
# - Draws from top to bottom in single pass
# - Uses constants for easy customization
#
# INTEGRATION WITH ORIGINAL CODE:
# - Called once during game setup in main.py
# - Doesn't interfere with game mechanics
# - Pure visual enhancement - no gameplay impact
# - Maintains Angela Yu's simple class structure
#
# This addition transforms the basic black screen into a proper
# pong court while preserving all of Angela Yu's core teaching
# concepts and game mechanics!
# =============================================================================