from typing import List, Dict
from da.types import Point

dirs = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
]


def solve(maze: List[str],
          wall: str,
          cur: Point,
          end: Point,
          seen: dict,
          path: List[Point]) -> bool:

    if cur.x == end.x and cur.y == end.y:
        path.append(end)
        return True

    if (cur.y < 0 or cur.y > len(maze) - 1 or
            cur.x < 0 or cur.x > len(maze[0]) - 1):
        return False

    if maze[cur.y][cur.x] == wall:
        return False

    if seen.get(f'{cur.x}_{cur.y}'):
        return False
    seen[f'{cur.x}_{cur.y}'] = True

    path.append(cur)
    for (x, y) in dirs:
        if solve(maze,
                 wall,
                 Point(x=cur.x + x, y=cur.y + y),
                 end,
                 seen,
                 path):
            return True

    path.pop()
    return False


def maze_solver(maze: List[str],
                wall: str,
                start: Point,
                end: Point) -> List[Point]:

    seen: dict = {}
    path: List[Point] = []
    solve(maze, wall, start, end, seen, path)
    return path
