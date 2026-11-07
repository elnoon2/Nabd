from smart_health.ai.astar import astar


def test_shortest_path_toy_graph():
    g = {"A": [("B", 1), ("C", 4)], "B": [("C", 2), ("D", 5)], "C": [("D", 1)], "D": []}
    cost, path = astar("A", lambda n: n == "D", lambda n: g[n], lambda n: 0)
    assert cost == 4 and path == ["A", "B", "C", "D"]


def test_unreachable():
    assert astar("A", lambda n: n == "Z", lambda n: [], lambda n: 0) is None
