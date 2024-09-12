from collections import deque


def is_valid(x, y, visited, board):
    if x < 0 or x >= 8 or y < 0 or y >= 8:
        return False
    if visited[x][y] or board[x][y] == '#':
        return False
    return True


def find_path(board):
    start = (0, 0)
    end = (7, 7)

    queue = deque()
    queue.append(start)

    visited = [[False for _ in range(8)] for _ in range(8)]
    visited[0][0] = True

    distance = [[0 for _ in range(8)] for _ in range(8)]
    while queue:

        curr_x, curr_y = queue.popleft()

        if (curr_x, curr_y) == end:
            return "YES " + str(distance[curr_x][curr_y])

        for dx, dy in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]:
            new_x = curr_x + dx
            new_y = curr_y + dy
            if is_valid(new_x, new_y, visited, board):
                queue.append((new_x, new_y))
                visited[new_x][new_y] = True
                distance[new_x][new_y] = distance[curr_x][curr_y] + 1
    return "NO"


board = []

for i in range(8):
    board.append(list(input()))

print(find_path(board))