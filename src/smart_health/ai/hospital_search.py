"""Hospital recommendation: A* over road graph + virtual goal node (cost = expected wait)."""
import math
from smart_health import config
from smart_health.ai.astar import astar
from smart_health.data.osm_loader import congestion_factor

GOAL = "__GOAL__"


def haversine_km(a, b):
    (la1, lo1), (la2, lo2) = a, b
    p = math.pi / 180
    h = (math.sin((la2 - la1) * p / 2) ** 2 +
         math.cos(la1 * p) * math.cos(la2 * p) * math.sin((lo2 - lo1) * p / 2) ** 2)
    return 2 * 6371 * math.asin(math.sqrt(h))


def recommend_hospital(G, start_node, hospitals, specialty, hour, expected_wait):
    """
    hospitals: dict hospital_id -> {"node": osm_node, "specialties": set, "latlon": (lat, lon)}
    expected_wait: callable (hospital_id, specialty, hour) -> minutes
    Returns (total_minutes, path_nodes, hospital_id) or None.
    """
    cf = congestion_factor(hour)
    node_to_h = {h["node"]: hid for hid, h in hospitals.items()}

    def neighbors(n):
        if n == GOAL:
            return
        for _, v, data in G.out_edges(n, data=True):
            yield v, data["travel_time"] / 60.0 * cf  # minutes
        if n in node_to_h:
            hid = node_to_h[n]
            wait = expected_wait(hid, specialty, hour)
            if specialty not in hospitals[hid]["specialties"]:
                wait += config.MISMATCH_PENALTY
            yield GOAL, wait

    def h(n):
        # TODO: admissible heuristic = straight-line km to nearest hospital / MAX_SPEED_KMH * 60
        return 0.0

    res = astar(start_node, lambda n: n == GOAL, neighbors, h)
    if not res:
        return None
    cost, path = res
    return cost, path[:-1], node_to_h[path[-2]]
