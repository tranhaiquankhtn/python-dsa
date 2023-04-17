

from da.graph.bfs import matrix_bfs
from .graph import matrix1


def test_graph_matrix_bfs():
    assert matrix_bfs(matrix1, 0, 6) == [
        0,
        1,
        4,
        5,
        6,
    ]
    assert matrix_bfs(matrix1, 6, 0) is None
