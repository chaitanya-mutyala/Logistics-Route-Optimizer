def visualize_route(csv_path, route):
    import matplotlib.pyplot as plt
    import networkx as nx
    import pandas as pd

    df = pd.read_csv(csv_path)
    G = nx.DiGraph()

    # Add edges and weights
    for _, row in df.iterrows():
        G.add_edge(row['source'], row['destination'], weight=row['distance'])

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)

    # Highlight the route
    route_edges = list(zip(route, route[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=route_edges, edge_color='red', width=3)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Optimized Route Visualization")
    plt.tight_layout()
    plt.show()
