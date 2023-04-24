from collections import deque
import random

def bfs(maze):
    queue = deque([(0, 0)])
    visited = set([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        if (x, y) == (4, 4):
            return True
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and maze[nx][ny] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    return False
def generate_maze(n):
    return [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]
maze = generate_maze(5)

maze[0][0] = 1
maze[4][4] = 1

# maze = [[1, 0, 1, 1, 0],
#         [1, 1, 0, 1, 0],
#         [0, 1, 1, 0, 1],
#         [0, 0, 1, 1, 1],
#         [1, 1, 0, 0, 1]]

print(maze[0])
print(maze[1])
print(maze[2])
print(maze[3])
print(bfs(maze))
