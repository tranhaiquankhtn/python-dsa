
from da.graph.dfs import matrix_dfs
from .graph import matrix1


def test_graph_matrix_dfs():
    assert matrix_dfs(matrix1, 0, 6) == [
        0,
        1,
        4,
        5,
        6,
    ]
    assert matrix_dfs(matrix1, 6, 0) is None
