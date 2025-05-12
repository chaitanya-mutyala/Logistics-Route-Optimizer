# src/predictor.py
import joblib
import pandas as pd

class TravelTimePredictor:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def preprocess(self, time_of_day, traffic_level):
        # Convert "18:00" → 18
        hour = int(time_of_day.split(":")[0])
        # Encode traffic level (same as during training)
        traffic_map = {"low": 0, "medium": 1, "high": 2}
        traffic_encoded = traffic_map.get(traffic_level.lower(), 1)
        return hour, traffic_encoded

    def predict(self, source, target, distance, time_of_day, traffic_level):
        hour, traffic_encoded = self.preprocess(time_of_day, traffic_level)
        features = pd.DataFrame([{
            "distance": distance,
            "hour": hour,
            "traffic_level_encoded": traffic_encoded
        }])
        return self.model.predict(features)[0]