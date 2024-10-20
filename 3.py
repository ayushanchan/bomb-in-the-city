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
GRAY = (192, 192, 192)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bomb in the City Game")
a_img = pygame.image.load('a.jpg')
def create_grid():
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    for i in range(GRID_SIZE):
       for j in range(GRID_SIZE):
            if random.random() < BOMB_PROBABILITY:
                grid[i][j] = 1
    return grid

def main():
    grid = create_grid()
    visited = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
    score = 0
    game_over = False

    running = True
    while running:
        screen.fill(WHITE)

        # Draw the grid
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, BLACK, rect, 1)  # Draw grid lines

                if visited[i][j]:
                    if grid[i][j] == 1:
                        pygame.draw.rect(screen, RED, rect)
                    else:
                        pygame.draw.rect(screen, GREEN, rect)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = pygame.mouse.get_pos()
                cell_x = x // CELL_SIZE
                cell_y = y // CELL_SIZE
                if not visited[cell_y][cell_x]:
                    visited[cell_y][cell_x] = True
                    if grid[cell_y][cell_x] == 1:
                        # Player hits a bomb
                        game_over = True
                    else:
                        # Player scores a point
                        score += 1

        # Display game over message with confetti
        if game_over:
            screen.blit(a_img,
                        (WIDTH // 2 - a_img.get_width() // 2, HEIGHT // 2 - a_img.get_height() // 2))
            pygame.display.flip()
            pygame.time.wait(3000)  
            print(f"Game over! Your score was: {score}")
            running = False


        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
