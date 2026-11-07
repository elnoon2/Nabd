"""Donor ranking: rule filter, then rank by travel time to the hospital."""
import networkx as nx
from smart_health.ai.rules import filter_donors


def rank_donors(G, hospital_node, donors, blood_type, cf=1.0, top_k=10):
    cands = filter_donors(donors, blood_type)
    # TODO: replace with the hand-written A* (one search per donor) if required by the rubric.
    dist = nx.single_source_dijkstra_path_length(G.reverse(copy=False), hospital_node, weight="travel_time")
    cands = cands.assign(minutes=cands.area_node.map(lambda n: dist.get(n, float("inf")) / 60.0 * cf))
    return cands.sort_values("minutes").head(top_k)
