
import pandas as pd
from dijkstra import RouteOptimizer
from visualize_route import visualize_route

def get_unique_nodes(csv_path):
    df = pd.read_csv(csv_path)
    sources = df['source'].unique()
    destinations = df['target'].unique()
    return sorted(set(sources).union(set(destinations)))

def valid_time_format(t):
    return len(t) == 5 and t[2] == ':' and t.replace(":", "").isdigit()

def main():
    print("🚚 Logistics Route Optimizer CLI 🚚")
    import pandas as pd

# Load the traffic data
    df = pd.read_csv("data/traffic_data.csv")  # Adjust path if needed

# Drop duplicates to get unique road segments
    city_graph_df = df[['source', 'target', 'distance']].drop_duplicates()

# Save to city_graph.csv
    city_graph_df.to_csv("data/city_graph.csv", index=False)

    csv_path = "data/traffic_data.csv"
    
    model_path = "ml/travel_time_model.pkl"

    optimizer = RouteOptimizer(csv_path, model_path)

    available_nodes = get_unique_nodes(csv_path)

    print("\nAvailable Cities:", ', '.join(available_nodes))

    source = input("\nEnter source node: ").strip().upper()
    while source not in available_nodes:
        print("❌ Invalid source node.")
        source = input("Enter source node again: ").strip().upper()

    destination = input("Enter destination node: ").strip().upper()
    while destination not in available_nodes:
        print("❌ Invalid destination node.")
        destination = input("Enter destination node again: ").strip().upper()
    

    time_of_day = input("Enter time of day (e.g., 08:00): ").strip()
    
    

    while not valid_time_format(time_of_day):
        print("❌ Invalid time format.")
        time_of_day = input("Enter time again (e.g., 08:00): ").strip()

    traffic_level = input("Enter traffic level (low / medium / high): ").strip().lower()
    while traffic_level not in ['low', 'medium', 'high']:
        print("❌ Invalid traffic level.")
        traffic_level = input("Enter traffic level (low / medium / high): ").strip().lower()

    try:
        route = optimizer.shortest_path(source, destination, time_of_day, traffic_level)
        print(f"\n✅ Optimized Route: {' -> '.join(route)}")

        show = input("Do you want to visualize the route? (y/n): ").strip().lower()
        if show == 'y':
            visualize_route(csv_path, route)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
