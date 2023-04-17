from collections import deque
from typing import List
from da.types import GraphEdge


def adj_bfs(graph: List[List[GraphEdge]], start: int, dest: int):
    def _bfs(curr: int, dest: int, seen: List[bool], prev: List[int]):
        q = deque([start])
        while q:
            curr = q.popleft()

            if curr == dest:
                break

            for edge in graph[curr]:
                if edge.weight == 0:
                    continue

                if seen[edge.to]:
                    continue

                seen[edge.to] = True
                prev[edge.to] = curr
                q.append(edge.to)

    seen: List[bool] = [False] * len(graph)
    prev: List[int] = [-1] * len(graph)

    seen[start] = True
    _bfs(start, dest, seen, prev)

    if prev[dest] == -1:
        return None

    paths = [dest]
    curr = prev[dest]
    while curr != -1:
        paths.append(curr)
        curr = prev[curr]

    return paths[::-1]


def matrix_bfs(matrix: List[List[int]], start: int, dest: int):
    prev: List[int] = [-1] * len(matrix)
    seen: List[bool] = [False] * len(matrix)

    q = deque([start])
    while q:
        curr = q.popleft()
        if curr == dest:
            break

        seen[curr] = True
        for i, e in enumerate(matrix[curr]):
            if e == 0:
                continue

            if seen[i]:
                continue

            prev[i] = curr
            q.append(i)
    curr = prev[dest]
    if curr == -1:
        return None

    paths = [dest]
    while curr != -1:
        paths.append(curr)
        curr = prev[curr]

    return paths[::-1]
