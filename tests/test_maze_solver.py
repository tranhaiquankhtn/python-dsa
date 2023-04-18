from typing import List
from da.graph.maze_solver import maze_solver
from da.types import Point


def test_maze_solver():
    maze: List[str] = [
        "xxxxxxxxxx x",
        "x        x x",
        "x        x x",
        "x xxxxxxxx x",
        "x          x",
        "x xxxxxxxxxx",
    ]

    maze_result: List[Point] = [
        Point(x=10, y=0),
        Point(x=10, y=1),
        Point(x=10, y=2),
        Point(x=10, y=3),
        Point(x=10, y=4),
        Point(x=9, y=4),
        Point(x=8, y=4),
        Point(x=7, y=4),
        Point(x=6, y=4),
        Point(x=5, y=4),
        Point(x=4, y=4),
        Point(x=3, y=4),
        Point(x=2, y=4),
        Point(x=1, y=4),
        Point(x=1, y=5),
    ]

    result = maze_solver(maze, "x", Point(x=10, y=0), Point(x=1, y=5))
    expected = draw_path(maze, maze_result)
    assert draw_path(maze, result) == expected


def draw_path(data: List[str], path: List[Point]) -> str:
    data2 = [[ch for ch in row] for row in data]
    for p in path:
        data2[p.y][p.x] = '*'
    return [''.join(row) for row in data2]
