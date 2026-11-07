"""Download Cairo road graph + hospitals from OpenStreetMap and cache to disk."""
import osmnx as ox
from smart_health import config


def congestion_factor(hour: int) -> float:
    """Simple hour-of-day multiplier on travel time."""
    if 7 <= hour <= 10 or 15 <= hour <= 19:
        return 1.8
    if 11 <= hour <= 14:
        return 1.3
    return 1.0


def load_graph():
    config.DATA_RAW.mkdir(parents=True, exist_ok=True)
    if config.GRAPH_CACHE.exists():
        return ox.load_graphml(config.GRAPH_CACHE)
    G = ox.graph_from_place(config.PLACE, network_type="drive")
    G = ox.add_edge_speeds(G)
    G = ox.add_edge_travel_times(G)
    ox.save_graphml(G, config.GRAPH_CACHE)
    return G


def load_hospitals():
    gdf = ox.features_from_place(config.PLACE, tags={"amenity": "hospital"})
    gdf = gdf.reset_index()
    gdf["lat"] = gdf.geometry.centroid.y
    gdf["lon"] = gdf.geometry.centroid.x
    return gdf[["name", "lat", "lon"]].dropna(subset=["lat", "lon"])


if __name__ == "__main__":
    G = load_graph()
    H = load_hospitals()
    H.to_csv(config.DATA_RAW / "hospitals.csv", index_label="hospital_id")
    print(f"Graph: {len(G)} nodes; hospitals: {len(H)}")
