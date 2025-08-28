import pygame
import random
import sys

# Screen dimensions
WIDTH, HEIGHT = 1366, 768
FONT_SIZE = 15
COLUMNS = WIDTH // FONT_SIZE
# Define multiple shades of green and black for variety
GREEN_SHADES = [
    (0, 255, 70),   # bright green (head)
    (0, 220, 60),
    (0, 180, 0),
    (0, 140, 0),
    (0, 100, 0)
]
BLACK_SHADES = [
    (0, 0, 0),
    (10, 10, 10),
    (20, 20, 20),
    (30, 30, 30),
    (40, 40, 40)
]
# Matrix characters (katakana, numbers, letters)
CHARS = "アイウエオカキクケコサシスセソタチツテトナニヌネノ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Give higher probability to katakana characters by repeating them in CHARS_POOL
KATAKANA = "アイウエオカキクケコサシスセソタチツテトナニヌネノ"
NUMBERS_LETTERS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHARS_POOL = KATAKANA * 5 + NUMBERS_LETTERS  # Katakana appears more often
class MatrixColumn:
    def __init__(self, x):
        self.x = x
        self.y = random.randint(-HEIGHT, 0)
        self.speed = random.randint(4, 10)
        self.chars = [random.choice(CHARS) for _ in range(HEIGHT // FONT_SIZE)]

    def draw(self, surface, font):
        for i, char in enumerate(self.chars):
            pos_y = self.y + i * FONT_SIZE
            if 0 <= pos_y < HEIGHT:
                color = (0, 255, 70) if i == 0 else (0, 180, 0)
                text = font.render(char, True, color)
                surface.blit(text, (self.x, pos_y))

    def update(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-HEIGHT, 0)
            self.chars = [random.choice(CHARS) for _ in range(HEIGHT // FONT_SIZE)]

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Matrix Code Rain")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Consolas", FONT_SIZE, bold=True)

    columns = [MatrixColumn(x * FONT_SIZE) for x in range(COLUMNS)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0, 10))
        for col in columns:
            col.draw(screen, font)
            col.update()

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()