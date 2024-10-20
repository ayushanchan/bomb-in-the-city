import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 10  # Number of cells in each row and column
CELL_SIZE = WIDTH // GRID_SIZE
BOMB_PROBABILITY = 0.1  # Probability of a cell containing a bomb

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bomb in the City Game")


# Function to create the grid with bombs randomly placed
def create_grid():
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if random.random() < BOMB_PROBABILITY:
                grid[i][j] = 1  # 1 indicates a bomb
    return grid


# Main game loop
def main():
    grid = create_grid()
    score = 0

    running = True
    while running:
        screen.fill(WHITE)

        # Draw the grid
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if grid[i][j] == 1:
                    pygame.draw.rect(screen, RED, rect)
                else:
                    pygame.draw.rect(screen, GREEN, rect)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                cell_x = x // CELL_SIZE
                cell_y = y // CELL_SIZE
                if grid[cell_y][cell_x] == 1:
                    # Player hits a bomb
                    print(f"Game over! Your score was: {score}")
                    running = False
                else:
                    # Player scores a point
                    score += 1
                    grid[cell_y][cell_x] = 2  # Mark cell as visited

        # Update the display
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
