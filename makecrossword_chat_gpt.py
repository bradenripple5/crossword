import random

def create_crossword(size):
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    words = ["python", "code", "crossword", "programming", "algorithm"]

    for word in words:
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            x = random.randint(0, size - len(word))
            y = random.randint(0, size - 1)
            for i, letter in enumerate(word):
                grid[y][x + i] = letter
        else:
            x = random.randint(0, size - 1)
            y = random.randint(0, size - len(word))
            for i, letter in enumerate(word):
                grid[y + i][x] = letter

    return grid

def display_crossword(grid):
    for row in grid:
        print(' '.join(row))

if __name__ == "__main__":
    size = 20
    crossword = create_crossword(size)
    display_crossword(crossword)
