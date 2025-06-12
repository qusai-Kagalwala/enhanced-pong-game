# =============================================================================
# Angela Yu's 100 Days of Code Challenge - Day 22: Enhanced Paddle Class
# Handles paddle creation, movement, and boundary checking with improvements
# =============================================================================

from turtle import Turtle

# =============================================================================
# PADDLE CONSTANTS (ADDED: Organized constants for better maintainability)
# =============================================================================
PADDLE_COLOR = "white"
PADDLE_SHAPE = "square"
PADDLE_WIDTH = 5  # stretch_wid parameter
PADDLE_LENGTH = 1  # stretch_len parameter
PADDLE_SPEED = 20
SCREEN_TOP_BOUNDARY = 250  # ADDED: Prevent paddle from going off screen
SCREEN_BOTTOM_BOUNDARY = -250  # ADDED: Prevent paddle from going off screen


class Paddle(Turtle):
    """
    ENHANCED Paddle class that creates and controls the game paddles
    Inherits from Turtle class for graphics

    ORIGINAL ANGELA YU VERSION: Basic paddle movement
    ENHANCED VERSION: Added boundary checking to prevent off-screen movement
    """

    def __init__(self, position):
        """
        Initialize paddle at given position
        ORIGINAL LOGIC: Unchanged from Angela Yu's implementation

        Args:
            position (tuple): (x, y) coordinates for paddle placement
        """
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH)
        self.penup()  # Don't draw lines when moving
        self.goto(position)

    def go_up(self):
        """
        Move paddle up with boundary checking
        ENHANCEMENT: Added boundary checking to prevent paddle going off screen

        ORIGINAL ANGELA YU CODE:
        def go_up(self):
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

        ENHANCED VERSION: Added boundary checking with constants
        """
        new_y = self.ycor() + PADDLE_SPEED

        # ADDED: Check boundary to prevent paddle going off screen
        if new_y <= SCREEN_TOP_BOUNDARY:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        """
        Move paddle down with boundary checking
        ENHANCEMENT: Added boundary checking to prevent paddle going off screen

        ORIGINAL ANGELA YU CODE:
        def go_down(self):
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

        ENHANCED VERSION: Added boundary checking with constants
        """
        new_y = self.ycor() - PADDLE_SPEED

        # ADDED: Check boundary to prevent paddle going off screen
        if new_y >= SCREEN_BOTTOM_BOUNDARY:
            self.goto(self.xcor(), new_y)

# =============================================================================
# CHANGES MADE TO ORIGINAL ANGELA YU CODE:
#
# ORIGINAL ANGELA YU IMPLEMENTATION:
# - Simple movement up/down by 20 pixels
# - No boundary checking - paddles could move off screen
# - Magic number 20 hardcoded in methods
# - Basic functionality only
#
# ENHANCED VERSION IMPROVEMENTS:
# 1. ✅ ADDED CONSTANTS: PADDLE_SPEED replaces magic number 20
# 2. ✅ BOUNDARY CHECKING: Paddles can't move off screen edges
# 3. ✅ SCREEN_BOUNDARIES: Added top/bottom boundary constants
# 4. ✅ BETTER DOCUMENTATION: Detailed docstrings and comments
# 5. ✅ MAINTAINED CORE LOGIC: Original movement mechanics preserved
#
# CORE ANGELA YU LOGIC PRESERVED:
# - Paddle initialization exactly the same
# - Movement direction logic unchanged
# - Turtle inheritance approach maintained
# - Same visual appearance and controls
#
# The enhanced version prevents the common issue where paddles
# disappear off the screen edges while maintaining Angela Yu's
# teaching structure and simplicity!
# =============================================================================