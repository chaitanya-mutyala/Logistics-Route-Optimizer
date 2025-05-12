import pandas as pd
import networkx as nx
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from predictor import TravelTimePredictor


class RouteOptimizer:
    def __init__(self, graph_file, model_file):
        self.graph = nx.DiGraph()
        self.load_graph(graph_file)
        self.predictor = TravelTimePredictor(model_file)

    def load_graph(self, graph_file):
        df = pd.read_csv(graph_file)
        for _, row in df.iterrows():
            self.graph.add_edge(row["source"], row["target"], distance=row["distance"])

    def predict_and_update_weights(self, time_of_day, traffic_level):
        for u, v, data in self.graph.edges(data=True):
            distance = data["distance"]
            predicted_time = self.predictor.predict(u, v, distance, time_of_day, traffic_level)
            self.graph[u][v]['weight'] = predicted_time  # Override weight

    def shortest_path(self, source, destination, time_of_day, traffic_level):
        self.predict_and_update_weights(time_of_day,traffic_level)

        return nx.dijkstra_path(self.graph, source, destination, weight='weight')
