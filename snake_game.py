import pygame
import sys
import random

# Initialize pygame
pygame.init()

# ---------- Game Constants ----------
WIDTH, HEIGHT = 600, 400       # Window size
BLOCK_SIZE = 20                # Size of snake segment and food
FPS = 10                       # Snake speed (increase for more difficulty)

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game (Python + Pygame)")
clock = pygame.time.Clock()

font_small = pygame.font.SysFont("consolas", 20)
font_big = pygame.font.SysFont("consolas", 40)


def draw_text(text, font, color, x, y, center=True):
    """Utility function to draw text on screen."""
    surface = font.render(text, True, color)
    rect = surface.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(surface, rect)


def random_food_position():
    """Return food position aligned to grid."""
    x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
    return x, y


def game_loop():
    # Initial snake settings
    snake_x = WIDTH // 2
    snake_y = HEIGHT // 2
    snake_body = [(snake_x, snake_y)]
    snake_length = 1

    # Initial movement (0: not moving)
    dx, dy = BLOCK_SIZE, 0  # moving right initially

    # Initial food position
    food_x, food_y = random_food_position()

    score = 0
    running = True
    game_over = False

    while running:
        while game_over:
            screen.fill(BLACK)
            draw_text("GAME OVER", font_big, RED, WIDTH // 2, HEIGHT // 2 - 40)
            draw_text(f"Score: {score}", font_small, WHITE, WIDTH // 2, HEIGHT // 2)
            draw_text("Press ENTER to play again or ESC to quit",
                      font_small, WHITE, WIDTH // 2, HEIGHT // 2 + 40)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Enter key
                        return  # restart game_loop
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

        # --------- Event Handling ---------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # Prevent immediate reverse direction
                if event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, BLOCK_SIZE
                elif event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = BLOCK_SIZE, 0

        # --------- Update Snake Position ---------
        snake_x += dx
        snake_y += dy

        head = (snake_x, snake_y)
        snake_body.append(head)

        # Keep snake_body length under control
        if len(snake_body) > snake_length:
            snake_body.pop(0)

        # --------- Collision: Wall ---------
        if (snake_x < 0 or snake_x >= WIDTH or
                snake_y < 0 or snake_y >= HEIGHT):
            game_over = True

        # --------- Collision: Self ---------
        if len(snake_body) != len(set(snake_body)):
            # If there are duplicates, snake hit itself
            game_over = True

        # --------- Collision: Food ---------
        if snake_x == food_x and snake_y == food_y:
            snake_length += 1
            score += 1
            food_x, food_y = random_food_position()

        # --------- Drawing ---------
        screen.fill(BLACK)

        # Draw food
        pygame.draw.rect(screen, RED, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))

        # Draw snake
        for segment in snake_body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

        # Draw score
        draw_text(f"Score: {score}", font_small, WHITE, 10, 10, center=False)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    while True:
        game_loop()  # Allows restart after game over
