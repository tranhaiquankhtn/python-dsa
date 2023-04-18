

from da.graph.dijkstra import dijkstra
from .graph import graph2


def test_dijkstra():
    assert dijkstra(graph2, 0, 6) == [0, 1, 4, 5, 6]
