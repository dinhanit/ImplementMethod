import heapq
def get_neighbors(x, y, matrix):
    neighbors = []
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Kiểm tra ô bên trái
    if x > 0 and matrix[x-1][y] == 0:
        neighbors.append((x-1, y))
    
    # Kiểm tra ô bên phải
    if x < rows - 1 and matrix[x+1][y] == 0:
        neighbors.append((x+1, y))
    
    # Kiểm tra ô phía trên
    if y > 0 and matrix[x][y-1] == 0:
        neighbors.append((x, y-1))
    
    # Kiểm tra ô phía dưới
    if y < cols - 1 and matrix[x][y+1] == 0:
        neighbors.append((x, y+1))
    
    return neighbors
def dijkstra(matrix, start, end):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Khởi tạo ma trận khoảng cách vô cùng lớn
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0
    
    # Khởi tạo ma trận đường đi
    path = [[None] * cols for _ in range(rows)]
    
    # Khởi tạo hàng đợi ưu tiên
    pq = [(0, start)]
    
    while pq:
        curr_dist, (x, y) = heapq.heappop(pq)
        
        # Đã đến đích
        if (x, y) == end:
            return build_path(path, start, end)
        
        # Kiểm tra các ô kề
        neighbors = get_neighbors(x, y, matrix)
        for nx, ny in neighbors:
            new_dist = curr_dist + 1  # Khoảng cách từ ô hiện tại đến ô kề là 1
            
            if new_dist < distances[nx][ny]:
                distances[nx][ny] = new_dist
                path[nx][ny] = (x, y)  # Lưu lại ô trước đó trên đường đi
                heapq.heappush(pq, (new_dist, (nx, ny)))
    
    return None  # Không tìm thấy đường đi

def build_path(path, start, end):
    current = end
    path_list = [current]
    
    while current != start:
        current = path[current[0]][current[1]]
        path_list.append(current)
    
    path_list.reverse()
    return path_list

# Ma trận ví dụ (0 là đường đi, 1 là vật cản)
matrix = [
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]

start = (0, 0)  # Vị trí bắt đầu
end = (4, 3)    # Vị trí kết thúc

path = dijkstra(matrix, start, end)

if path is None:
    print("Không tìm thấy đường đi")
else:
    print("Đường đi ngắn nhất:")
    for point in path:
        print(point)
