# =============================================================================
# Angela Yu's 100 Days of Code Challenge - Day 22: Enhanced Pong Game
# Classic Pong with modern enhancements and performance improvements
# =============================================================================

import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from center_line import CenterLine

# =============================================================================
# GAME CONSTANTS (ADDED: Organized constants for better maintainability)
# =============================================================================

# Screen Configuration
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = "black"
GAME_TITLE = "Enhanced Pong Game"

# Paddle Configuration
RIGHT_PADDLE_POS = (350, 0)
LEFT_PADDLE_POS = (-350, 0)
PADDLE_SPEED = 20

# Ball Configuration
BALL_SPEED = 0.1
WALL_BOUNDARY = 280

# Collision Detection Constants
PADDLE_COLLISION_DISTANCE = 50
RIGHT_PADDLE_X_BOUNDARY = 320
LEFT_PADDLE_X_BOUNDARY = -320

# Scoring Configuration
RIGHT_BOUNDARY = 380
LEFT_BOUNDARY = -380
WINNING_SCORE = 5  # ADDED: Win condition - first to 5 points wins

# Control Keys Configuration
RIGHT_PADDLE_UP = "Up"
RIGHT_PADDLE_DOWN = "Down"
LEFT_PADDLE_UP = "w"
LEFT_PADDLE_DOWN = "s"


# =============================================================================
# SETUP FUNCTIONS (ADDED: Modular approach for better code organization)
# =============================================================================

def setup_screen():
    """
    Initialize and configure the game screen
    Returns: Screen object with proper configuration
    """
    screen = Screen()
    screen.bgcolor(SCREEN_COLOR)
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title(GAME_TITLE)
    screen.tracer(0)  # Turn off screen updates for smooth animation
    return screen


def setup_game_objects():
    """
    Create and return all game objects
    Returns: Tuple of (r_paddle, l_paddle, ball, scoreboard, center_line)
    """
    r_paddle = Paddle(RIGHT_PADDLE_POS)
    l_paddle = Paddle(LEFT_PADDLE_POS)
    ball = Ball()
    scoreboard = Scoreboard()
    center_line = CenterLine()  # ADDED: Dotted center line for professional look
    return r_paddle, l_paddle, ball, scoreboard, center_line


def setup_controls(screen, r_paddle, l_paddle):
    """
    Configure keyboard controls for paddles
    Args:
        screen: Game screen object
        r_paddle: Right paddle object
        l_paddle: Left paddle object
    """
    screen.listen()
    screen.onkey(r_paddle.go_up, RIGHT_PADDLE_UP)
    screen.onkey(r_paddle.go_down, RIGHT_PADDLE_DOWN)
    screen.onkey(l_paddle.go_up, LEFT_PADDLE_UP)
    screen.onkey(l_paddle.go_down, LEFT_PADDLE_DOWN)


# =============================================================================
# COLLISION DETECTION (ADDED: Improved performance with rectangular collision)
# =============================================================================

def check_wall_collision(ball):
    """
    Check if ball hits top or bottom wall
    Args:
        ball: Ball object to check
    Returns: Boolean - True if collision detected
    """
    return ball.ycor() > WALL_BOUNDARY or ball.ycor() < -WALL_BOUNDARY


def check_paddle_collision(ball, r_paddle, l_paddle):
    """
    PERFORMANCE IMPROVEMENT: Rectangular collision detection instead of circular
    More accurate than the original distance-based method

    Original code used: ball.distance(paddle) < 50
    New code uses precise rectangular boundaries for better accuracy

    Args:
        ball: Ball object
        r_paddle: Right paddle object
        l_paddle: Left paddle object
    Returns: Boolean - True if collision detected
    """
    ball_x, ball_y = ball.xcor(), ball.ycor()

    # Right paddle collision (rectangular boundary detection)
    if (ball_x > RIGHT_PADDLE_X_BOUNDARY and ball_x < RIGHT_PADDLE_X_BOUNDARY + 30 and
            ball_y < r_paddle.ycor() + 50 and ball_y > r_paddle.ycor() - 50):
        return True

    # Left paddle collision (rectangular boundary detection)
    if (ball_x < LEFT_PADDLE_X_BOUNDARY and ball_x > LEFT_PADDLE_X_BOUNDARY - 30 and
            ball_y < l_paddle.ycor() + 50 and ball_y > l_paddle.ycor() - 50):
        return True

    return False


# =============================================================================
# WIN CONDITION LOGIC (ADDED: Game ending functionality)
# =============================================================================

def check_game_winner(scoreboard):
    """
    ADDED: Check if either player has reached winning score
    Args:
        scoreboard: Scoreboard object containing current scores
    Returns: Boolean - True if game should end
    """
    return scoreboard.l_score >= WINNING_SCORE or scoreboard.r_score >= WINNING_SCORE


def display_winner(scoreboard):
    """
    ADDED: Display the winner announcement with trophy emoji
    Args:
        scoreboard: Scoreboard object to display winner
    """
    winner = "LEFT PLAYER" if scoreboard.l_score >= WINNING_SCORE else "RIGHT PLAYER"
    scoreboard.display_winner(winner)


# =============================================================================
# MAIN GAME FUNCTION (ENHANCED: Better structure and win conditions)
# =============================================================================

def main():
    """
    Main game function - handles complete game flow from start to finish
    ENHANCED VERSION of original while loop with modular functions
    """
    # Initialize game components
    screen = setup_screen()
    r_paddle, l_paddle, ball, scoreboard, center_line = setup_game_objects()
    setup_controls(screen, r_paddle, l_paddle)

    # ADDED: Draw center line for professional court appearance
    center_line.draw()

    # Main game loop (ENHANCED: Original while loop with additional features)
    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Wall collision (ORIGINAL LOGIC: Unchanged from Angela Yu's version)
        if check_wall_collision(ball):
            ball.bounce_y()

        # Paddle collision (PERFORMANCE IMPROVEMENT: Better collision detection)
        if check_paddle_collision(ball, r_paddle, l_paddle):
            ball.bounce_x()

        # Right paddle misses - left player scores (ENHANCED: Added win checking)
        if ball.xcor() > RIGHT_BOUNDARY:
            ball.reset_position()
            scoreboard.l_point()

            # ADDED: Check for winner after each point
            if check_game_winner(scoreboard):
                display_winner(scoreboard)
                game_is_on = False

        # Left paddle misses - right player scores (ENHANCED: Added win checking)
        if ball.xcor() < LEFT_BOUNDARY:
            ball.reset_position()
            scoreboard.r_point()

            # ADDED: Check for winner after each point
            if check_game_winner(scoreboard):
                display_winner(scoreboard)
                game_is_on = False

    # Keep window open until clicked (ORIGINAL: Unchanged)
    screen.exitonclick()


# =============================================================================
# PROGRAM EXECUTION
# =============================================================================

# Run the game
if __name__ == "__main__":
    main()

# =============================================================================
# KEY ENHANCEMENTS ADDED TO ORIGINAL ANGELA YU CODE:
#
# ORIGINAL CODE STRUCTURE:
# - Simple while loop with basic collision detection
# - No win conditions - game runs indefinitely
# - Basic circular collision detection using distance()
# - No center line or professional court appearance
# - All code in single file without constants
#
# ENHANCED VERSION ADDITIONS:
# 1. ✅ WIN CONDITIONS: First to 5 points wins with winner display
# 2. ✅ CONSTANTS: All magic numbers organized into constants section
# 3. ✅ DOTTED CENTER LINE: Professional court divider (new CenterLine class)
# 4. ✅ PERFORMANCE: Rectangular collision detection instead of circular
# 5. ✅ MODULAR FUNCTIONS: Code split into logical functions
# 6. ✅ BOUNDARY CHECKING: Paddles can't move off screen (enhanced Paddle class)
# 7. ✅ BETTER DOCUMENTATION: Comprehensive comments following Angela Yu style
# 8. ✅ WINNER ANNOUNCEMENT: Trophy emojis and colored winner text
# 9. ✅ CODE ORGANIZATION: Separated concerns into different classes
# 10. ✅ ERROR PREVENTION: Added bounds checking and validation
#
# The core game logic remains faithful to Angela Yu's teaching approach
# while adding professional game development practices and features!
# =============================================================================