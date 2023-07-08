import numpy as np
from collections import deque

def find_path(matrix, start, end):
    rows, cols = matrix.shape

    # Helper function to check if a cell is valid and not a barrier
    def is_valid_cell(row, col):
        return 0 <= row < rows and 0 <= col < cols and matrix[row, col] != 255

    # Possible directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Keep track of visited cells
    visited = np.zeros((rows, cols), dtype=bool)
    visited[start] = True

    # Queue for BFS traversal
    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()
        row, col = current

        # Check if we reached the end point
        if current == end:
            return path + [current]

        # Explore the neighboring cells
        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]

            if is_valid_cell(new_row, new_col) and not visited[new_row, new_col]:
                visited[new_row, new_col] = True
                queue.append(((new_row, new_col), path + [current]))

    # No path found
    return None
