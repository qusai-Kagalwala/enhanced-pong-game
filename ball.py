# =============================================================================
# Angela Yu's 100 Days of Code Challenge - Day 22: Enhanced Ball Class
# Handles ball movement, bouncing, and speed control with improvements
# =============================================================================

from turtle import Turtle

# =============================================================================
# BALL CONSTANTS (ADDED: Organized constants for better maintainability)
# =============================================================================
BALL_COLOR = "white"
BALL_SHAPE = "circle"
INITIAL_MOVE_DISTANCE = 10
INITIAL_MOVE_SPEED = 0.1
SPEED_INCREASE_FACTOR = 0.9  # ENHANCED: Ball gets faster after each paddle hit


class Ball(Turtle):
    """
    ENHANCED Ball class that handles the pong ball behaviour
    Inherits from Turtle class for graphics

    ORIGINAL ANGELA YU VERSION: Basic movement and bouncing
    ENHANCED VERSION: Added constants, better documentation, same core logic
    """

    def __init__(self):
        """
        Initialize the ball with starting properties
        ORIGINAL LOGIC: Unchanged from Angela Yu's implementation
        """
        super().__init__()
        self.color(BALL_COLOR)
        self.shape(BALL_SHAPE)
        self.penup()  # Don't draw lines when moving

        # Movement attributes (ORIGINAL: Same as Angela Yu's version)
        self.x_move = INITIAL_MOVE_DISTANCE
        self.y_move = INITIAL_MOVE_DISTANCE
        self.move_speed = INITIAL_MOVE_SPEED

    def move(self):
        """
        Move the ball by updating its position
        ORIGINAL ANGELA YU LOGIC: Exactly the same implementation

        Fixed spacing issue from original code:
        OLD: new_y = self.ycor() + self .y_move  # Extra space before .y_move
        NEW: new_y = self.ycor() + self.y_move   # Proper spacing
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move  # FIXED: Removed extra space
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Bounce ball off top and bottom walls
        ORIGINAL LOGIC: Unchanged from Angela Yu's version
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Bounce ball off paddles and increase speed
        ORIGINAL LOGIC: Unchanged from Angela Yu's version

        Speed increases each time ball hits a paddle using SPEED_INCREASE_FACTOR
        This makes the game progressively more challenging
        """
        self.x_move *= -1
        self.move_speed *= SPEED_INCREASE_FACTOR

    def reset_position(self):
        """
        Reset ball to center after a point is scored
        ORIGINAL LOGIC: Unchanged from Angela Yu's version

        Also reset speed and reverse direction for next serve
        """
        self.goto(0, 0)
        self.move_speed = INITIAL_MOVE_SPEED
        self.bounce_x()  # Change direction for next serve

# =============================================================================
# CHANGES MADE TO ORIGINAL ANGELA YU CODE:
#
# ORIGINAL CODE ISSUES FIXED:
# 1. ❌ new_y = self.ycor() + self .y_move  # Extra space before .y_move
# 2. ❌ No constants - magic numbers scattered throughout
# 3. ❌ Minimal documentation
#
# ENHANCED VERSION IMPROVEMENTS:
# 1. ✅ FIXED SPACING: Proper spacing in move() method
# 2. ✅ ADDED CONSTANTS: All magic numbers moved to constants section
# 3. ✅ BETTER DOCUMENTATION: Comprehensive docstrings and comments
# 4. ✅ MAINTAINED LOGIC: All original Angela Yu logic preserved
#
# CORE FUNCTIONALITY UNCHANGED:
# - Ball movement mechanics identical to original
# - Bouncing physics exactly the same
# - Speed increase system unchanged
# - Reset functionality preserved
#
# The enhanced version maintains Angela Yu's teaching approach while
# adding professional coding practices and fixing minor syntax issues!
# =============================================================================