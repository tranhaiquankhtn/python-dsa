from typing import List
from da.types import GraphEdge


def adj_dfs(graph: List[List[GraphEdge]], start: int, dest: int):
    def _dfs(curr: int, dest: int, seen: List[bool], paths: List[int]) -> bool:
        if curr == dest:
            paths.append(dest)
            return True

        seen[curr] = True
        paths.append(curr)
        for edge in graph[curr]:
            if edge.weight == 0:
                continue

            if seen[edge.to]:
                continue

            if _dfs(edge.to, dest, seen, paths):
                return True
        paths.pop()
        return False

    paths = []
    seen: List[bool] = [False] * len(graph)
    seen[start] = True
    _dfs(start, dest, seen, paths)
    return paths if paths else None


def matrix_dfs(matrix: List[List[int]], start: int, dest: int):
    def _dfs(curr: int, dest: int, seen: List[bool], paths: List[int]) -> bool:
        paths.append(curr)
        if curr == dest:
            return True

        seen[curr] = True
        for i, e in enumerate(matrix[curr]):
            if e == 0:
                continue

            if seen[i]:
                continue

            if _dfs(i, dest, seen, paths):
                return True
        paths.pop()
        return False

    paths: List[int] = []
    seen: List[bool] = [False] * len(matrix)
    seen[start] = True
    _dfs(start, dest, seen, paths)
    return paths if paths else None
