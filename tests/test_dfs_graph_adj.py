
from da.graph.dfs import adj_dfs
from .graph import graph1


def test_graph_adjcent_dfs():
    assert adj_dfs(graph1, 0, 6) == [
        0,
        1,
        4,
        5,
        6,
    ]
    assert adj_dfs(graph1, 6, 0) is None
