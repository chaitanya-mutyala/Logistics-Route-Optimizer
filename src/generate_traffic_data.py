import pandas as pd
import numpy as np
import os

# Load the city graph
graph_path = os.path.join(os.path.dirname(__file__), "../data/city_graph.csv")
df = pd.read_csv(graph_path)

# Time slots and traffic levels
times = ["06:00", "09:00", "12:00", "15:00", "18:00", "21:00"]
traffic_levels = ["low", "medium", "high"]

# Generate synthetic data
rows = []
for _, row in df.iterrows():
    for time in times:
        for level in traffic_levels:
            base = row['distance']
            # Simulated variation in travel time
            factor = {
                "low": np.random.uniform(1.0, 1.2),
                "medium": np.random.uniform(1.3, 1.6),
                "high": np.random.uniform(1.7, 2.0),
            }[level]
            travel_time = round(base * factor, 2)
            rows.append({
                "source": row['source'],
                "target": row['destination'],
                "distance": base,
                "time_of_day": time,
                "traffic_level": level,
                "travel_time": travel_time
            })

traffic_df = pd.DataFrame(rows)

# Save to CSV
out_path = os.path.join(os.path.dirname(__file__), "../data/traffic_data.csv")
traffic_df.to_csv(out_path, index=False)

print(f"[✅] Generated traffic data with {len(traffic_df)} rows and saved to: {out_path}")
