import random

def generate_maze(width, height):
    """
    Generate a maze using a recursive backtracking algorithm.
    The maze will be represented as a 2D list of cells,
    where True indicates a passage and False indicates a wall.
    The final ASCII output grid will be of size (2*height + 1) × (2*width + 1).
    """
    # Initialize a grid of cells, all unvisited
    visited = [[False for _ in range(width)] for _ in range(height)]
    # Directions: (dx, dy) for N, S, W, E
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # This will store the carved paths between cells
    # Output grid: start all as walls
    output = [[False for _ in range(width * 2 + 1)] for _ in range(height * 2 + 1)]

    def carve(x, y):
        """Recursive function to carve passages from cell (x, y)."""
        visited[y][x] = True
        # Mark the cell itself as a passage
        output[y * 2 + 1][x * 2 + 1] = True

        # Randomize directions to get a random maze
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check bounds and if the neighbor is unvisited
            if 0 <= nx < width and 0 <= ny < height and not visited[ny][nx]:
                # Carve a passage between (x, y) and (nx, ny)
                output[y * 2 + 1 + dy][x * 2 + 1 + dx] = True
                carve(nx, ny)

    # Start carving from the top-left cell (0, 0)
    carve(0, 0)
    return output

def print_maze(output):
    """
    Given the output grid (2D list of booleans), print an ASCII maze:
    '#' for walls (False) and ' ' for passages (True).
    """
    for row in output:
        print("".join(' ' if cell else '█' for cell in row))

if __name__ == "__main__":
    # Example usage: a 10×5 maze (i.e., 10 cells wide, 5 cells tall)
    width, height = 10, 5
    maze = generate_maze(width, height)
    print_maze(maze)
    
