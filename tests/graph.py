from typing import List
from da.types import GraphEdge

#     >(1)<--->(4) ---->(5)
#    /          |       /|
# (0)     ------|------- |
#    \   v      v        v
#     >(2) --> (3) <----(6)
graph1: List[List[GraphEdge]] = [
    [
        GraphEdge(to=1, weight=3),
        GraphEdge(to=2, weight=1),
    ],
    [
        GraphEdge(to=4, weight=1),
    ],
    [
        GraphEdge(to=3, weight=7),
    ],
    [],
    [
        GraphEdge(to=1, weight=1),
        GraphEdge(to=3, weight=5),
        GraphEdge(to=5, weight=2),
    ],
    [
        GraphEdge(to=2, weight=18),
        GraphEdge(to=6, weight=1),
    ],
    [
        GraphEdge(to=3, weight=1),
    ],
]

matrix1: List[List[int]] = [
    [0, 3, 1,  0, 0, 0, 0],
    [0, 0, 0,  0, 1, 0, 0],
    [0, 0, 7,  0, 0, 0, 0],
    [0, 0, 0,  0, 0, 0, 0],
    [0, 1, 0,  5, 0, 2, 0],
    [0, 0, 18, 0, 0, 0, 1],
    [0, 0, 0,  1, 0, 0, 1]
]
