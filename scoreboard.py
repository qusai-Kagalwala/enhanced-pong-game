# =============================================================================
# Angela Yu's 100 Days of Code Challenge - Day 22: Enhanced Scoreboard Class
# Handles score display, winner announcement, and game state with improvements
# =============================================================================

from turtle import Turtle

# =============================================================================
# SCOREBOARD CONSTANTS (ADDED: Organized constants for better maintainability)
# =============================================================================
SCOREBOARD_COLOR = "white"
SCORE_FONT = ("Courier", 80, "normal")
WINNER_FONT = ("Courier", 36, "bold")  # ADDED: Font for winner announcement
LEFT_SCORE_POSITION = (-100, 200)
RIGHT_SCORE_POSITION = (100, 200)
WINNER_POSITION = (0, 0)  # ADDED: Position for winner text
ALIGNMENT = "center"


class Scoreboard(Turtle):
    """
    ENHANCED Scoreboard class that manages game scoring and winner display
    Inherits from Turtle class for text display

    ORIGINAL ANGELA YU VERSION: Basic score tracking and display
    ENHANCED VERSION: Added winner announcement functionality
    """

    def __init__(self):
        """
        Initialize scoreboard with starting scores
        ORIGINAL LOGIC: Unchanged from Angela Yu's implementation
        """
        super().__init__()
        self.color(SCOREBOARD_COLOR)
        self.penup()  # Don't draw lines
        self.hideturtle()  # Hide the turtle cursor

        # Score tracking (ORIGINAL: Same as Angela Yu's version)
        self.l_score = 0
        self.r_score = 0

        # Display initial scores
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Update the scoreboard display with current scores
        ORIGINAL ANGELA YU LOGIC: Exactly the same implementation
        """
        self.clear()  # Clear previous display

        # Display left player score
        self.goto(LEFT_SCORE_POSITION)
        self.write(self.l_score, align=ALIGNMENT, font=SCORE_FONT)

        # Display right player score
        self.goto(RIGHT_SCORE_POSITION)
        self.write(self.r_score, align=ALIGNMENT, font=SCORE_FONT)

    def l_point(self):
        """
        Add point to left player and update display
        ORIGINAL LOGIC: Unchanged from Angela Yu's version
        Called when right paddle misses the ball
        """
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """
        Add point to right player and update display
        ORIGINAL LOGIC: Unchanged from Angela Yu's version
        Called when left paddle misses the ball
        """
        self.r_score += 1
        self.update_scoreboard()

    def display_winner(self, winner):
        """
        ADDED: Display the winner announcement with trophy emojis
        This is completely new functionality not in Angela Yu's original

        Args:
            winner (str): Name of the winning player
        """
        self.goto(WINNER_POSITION)
        self.color("yellow")  # ADDED: Highlight winner text in yellow
        self.write(f"🏆 {winner} WINS! 🏆\nClick to exit",
                   align=ALIGNMENT, font=WINNER_FONT)

# =============================================================================
# CHANGES MADE TO ORIGINAL ANGELA YU CODE:
#
# ORIGINAL ANGELA YU IMPLEMENTATION:
# class Scoreboard(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.color("white")
#         self.penup()
#         self.hideturtle()
#         self.l_score = 0
#         self.r_score = 0
#         self.update_scoreboard()
#
#     def update_scoreboard(self):
#         self.clear()
#         self.goto(-100, 200)
#         self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
#         self.goto(100, 200)
#         self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
#
#     def l_point(self):
#         self.l_score += 1
#         self.update_scoreboard()
#
#     def r_point(self):
#         self.r_score += 1
#         self.update_scoreboard()
#
# ENHANCED VERSION IMPROVEMENTS:
# 1. ✅ ADDED CONSTANTS: All magic numbers moved to constants section
# 2. ✅ WINNER DISPLAY: New display_winner() method with trophy emojis
# 3. ✅ WINNER FONT: Separate font styling for winner announcement
# 4. ✅ COLOR HIGHLIGHT: Winner text displayed in yellow for emphasis
# 5. ✅ BETTER DOCUMENTATION: Comprehensive docstrings and comments
# 6. ✅ MAINTAINED CORE LOGIC: All original Angela Yu functionality preserved
#
# ORIGINAL FUNCTIONALITY UNCHANGED:
# - Score initialization and tracking identical
# - update_scoreboard() method exactly the same
# - l_point() and r_point() methods unchanged
# - Same font, positioning, and display logic
#
# NEW FUNCTIONALITY ADDED:
# - Winner announcement with trophy emojis 🏆
# - Color-coded winner display (yellow highlight)
# - Professional game completion message
# - Exit instructions for players
#
# The enhanced version maintains Angela Yu's simple and effective
# approach while adding the game completion functionality that
# makes it feel like a complete, polished game!
# =============================================================================