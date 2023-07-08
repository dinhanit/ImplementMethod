import cv2
import numpy as np
from collections import deque

start = None
end = None

def mouse_callback(event, x, y, flags, param):
    global start, end
    
    if event == cv2.EVENT_LBUTTONDOWN:
        if start is None:
            start = (y, x)
            print("Điểm bắt đầu:", start)
        elif end is None:
            end = (y, x)
            print("Điểm kết thúc:", end)

image = cv2.imread('Maze.png', 0)

maze = np.where(image < 128, 1, 0)

height, width = maze.shape

def is_valid(cell):
    x, y = cell
    return 0 <= x < height and 0 <= y < width and maze[x, y] == 0

def solve_maze_bfs(start, end):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        current_cell, path = queue.popleft()
        if current_cell == end:
            return path + [current_cell]

        if current_cell in visited:
            continue

        visited.add(current_cell)

        x, y = current_cell
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for neighbor in neighbors:
            if is_valid(neighbor):
                queue.append((neighbor, path + [current_cell]))

    return None

cv2.namedWindow('Maze')
cv2.setMouseCallback('Maze', mouse_callback)

while True:
    cv2.imshow('Maze', image)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    
    if start is not None and end is not None:
        solution_path = solve_maze_bfs(start, end)
        
        if solution_path is None:
            print("Không tìm thấy đường đi trong mê cung.")
        else:
            result_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
            for cell in solution_path:
                cv2.circle(result_image, (cell[1], cell[0]), 1, (0, 0, 255), -1)

            cv2.imshow('Maze Solution', result_image)
            
            start = None
            end = None

cv2.destroyAllWindows()
