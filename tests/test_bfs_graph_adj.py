from da.graph.bfs import adj_bfs
from .graph import graph1


def test_graph_adjcent_bfs():
    assert adj_bfs(graph1, 0, 6) == [
        0,
        1,
        4,
        5,
        6,
    ]
    assert adj_bfs(graph1, 6, 0) is None
