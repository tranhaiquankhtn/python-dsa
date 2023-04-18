import math
from typing import List, Optional
from da.types import GraphEdge

INF = math.inf


def has_unvisited(seen: List[bool], dists: List[int]) -> bool:
    return any(not visited and dists[i] < INF for i, visited in enumerate(seen))


def get_min_dist_vertex(seen: List[bool], dists: List[int]) -> int:
    idx = -1
    cur_dist = INF

    for i, visited in enumerate(seen):
        if visited:
            continue

        if cur_dist > dists[i]:
            cur_dist = dists[i]
            idx = i
    return idx


def dijkstra(graph: List[List[GraphEdge]], start: int, dest: int) -> List[int]:
    seen = [False] * len(graph)
    prev = [-1] * len(graph)
    dists = [INF] * len(graph)

    dists[start] = 0
    while has_unvisited(seen, dists):
        curr = get_min_dist_vertex(seen, dists)
        seen[curr] = True

        for edge in graph[curr]:
            if seen[edge.to]:
                continue

            dist = dists[curr] + edge.weight
            if dist < dists[edge.to]:
                dists[edge.to] = dist
                prev[edge.to] = curr
    # rebuild path
    if prev[dest] == -1:
        return []

    paths = [dest]
    curr = prev[dest]
    while curr != -1:
        paths.append(curr)
        curr = prev[curr]
    return paths[::-1]
