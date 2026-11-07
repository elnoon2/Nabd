"""A* implemented by hand with a priority queue (heapq)."""
import heapq
import itertools
from typing import Callable, Dict, Hashable, Iterable, Optional, Tuple


def astar(start: Hashable,
          is_goal: Callable[[Hashable], bool],
          neighbors: Callable[[Hashable], Iterable[Tuple[Hashable, float]]],
          heuristic: Callable[[Hashable], float]) -> Optional[Tuple[float, list]]:
    """neighbors(node) -> iterable of (next_node, cost). Returns (total_cost, path) or None."""
    counter = itertools.count()  # tie-breaker so nodes are never compared
    open_heap = [(heuristic(start), next(counter), 0.0, start)]
    g: Dict[Hashable, float] = {start: 0.0}
    parent: Dict[Hashable, Hashable] = {}
    closed = set()
    while open_heap:
        _, _, g_cur, cur = heapq.heappop(open_heap)
        if cur in closed:
            continue
        if is_goal(cur):
            path = [cur]
            while cur in parent:
                cur = parent[cur]
                path.append(cur)
            return g_cur, path[::-1]
        closed.add(cur)
        for nxt, cost in neighbors(cur):
            ng = g_cur + cost
            if ng < g.get(nxt, float("inf")):
                g[nxt] = ng
                parent[nxt] = cur
                heapq.heappush(open_heap, (ng + heuristic(nxt), next(counter), ng, nxt))
    return None
