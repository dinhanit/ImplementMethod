import cv2
import numpy as np
from collections import deque

# Biến toàn cục để lưu các tọa độ điểm bắt đầu và kết thúc
start = None
end = None

# Callback function cho sự kiện click chuột
def mouse_callback(event, x, y, flags, param):
    global start, end
    
    if event == cv2.EVENT_LBUTTONDOWN:
        if start is None:
            start = (y, x)  # Hoán đổi tọa độ x và y vì OpenCV sử dụng thứ tự ngược lại
            print("Điểm bắt đầu:", start)
        elif end is None:
            end = (y, x)
            print("Điểm kết thúc:", end)

# Đọc ảnh
image = cv2.imread('mecung.jpg', 0)  # Chuyển ảnh thành ảnh grayscale

# Tạo ma trận mê cung từ ảnh
maze = np.where(image < 128, 1, 0)

# Kích thước của mê cung
height, width = maze.shape

# Hàm kiểm tra xem một ô có hợp lệ hay không
def is_valid(cell):
    x, y = cell
    return 0 <= x < height and 0 <= y < width and maze[x, y] == 0

# Tìm đường đi trong mê cung sử dụng BFS
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

# Tạo cửa sổ hiển thị ảnh và liên kết callback function
cv2.namedWindow('Maze')
cv2.setMouseCallback('Maze', mouse_callback)

while True:
    # Hiển thị ảnh
    cv2.imshow('Maze', image)
    
    # Đợi phím nhấn từ người dùng
    key = cv2.waitKey(1) & 0xFF
    
    # Thoát chương trình nếu nhấn phím 'q'
    if key == ord('q'):
        break
    
    # Giải mê cung khi đã chọn đủ điểm bắt đầu và kết thúc
    if start is not None and end is not None:
        # Giải mê cung
        solution_path = solve_maze_bfs(start, end)
        
        if solution_path is None:
            print("Không tìm thấy đường đi trong mê cung.")
        else:
            # Tạo ảnh kết quả với đường đi được vẽ lên
            result_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
            for cell in solution_path:
                cv2.circle(result_image, (cell[1], cell[0]), 2, (0, 0, 255), -1)

            # Hiển thị ảnh kết quả
            cv2.imshow('Maze Solution', result_image)
            
            # Đặt lại các điểm bắt đầu và kết thúc để cho phép người dùng chọn lại
            start = None
            end = None

# Đóng tất cả các cửa sổ hiển thị
cv2.destroyAllWindows()
