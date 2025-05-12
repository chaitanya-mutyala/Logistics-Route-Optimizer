# 🚚 Logistics Route Optimizer

This project finds the optimal delivery route between cities based on traffic conditions and time of day, using **Dijkstra's algorithm** and a **Machine Learning model** to predict travel time.

---

## 🔧 Features

- Predicts travel time using a trained ML model (.pkl)
- Dijkstra's algorithm for shortest path with updated weights
- CLI interface for real-time interaction
- Graph route visualization using matplotlib
- Jupyter Notebook included to retrain ML model on custom CSV

---

## 📁 Repository Structure

```
Logistics-Route-Optimizer/
│
├── data/
│   └── routes.csv                # Source/destination pairs with distance & travel info
│
├── src/
│   ├── cli.py                    # CLI entry-point for user interaction
│   ├── dijkstra.py              # RouteOptimizer class with Dijkstra logic
│   ├── predictor.py             # TravelTimePredictor using a trained .pkl model
│   └── visualize_route.py       # Route and graph plotting using matplotlib
│
├── notebooks/
│   └── train_model.ipynb        # Jupyter notebook to train new ML model
│
├── ml/
│   └── travel_time_model.pkl    # Pre-trained model used by predictor.py
│
├── requirements.txt             # Required Python packages
└── README.md                    # Project overview and usage instructions
```

---

## 🧠 Algorithm & ML Integration

1. **Dijkstra’s Algorithm** is used to find the shortest path.
2. Instead of using static distances as edge weights, we pass source, destination, distance, `time_of_day`, and `traffic_level` to an ML model.
3. The ML model predicts travel time which is used as the weight.
4. This allows routing to adapt to real-time conditions.

---

## 💻 How to Use

### 1. Clone the repository
```bash
git clone <repo-url>
cd Logistics-Route-Optimizer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the CLI interface
```bash
python src/cli.py
```
You will be prompted to enter:
- Source node
- Destination node
- Time of day (e.g., 08:00)
- Traffic level (low / medium / high)

### 4. Visualize Route (optional)
```bash
python src/visualize_route.py
```

---

## 📊 Train with Your Own Data

1. Go to the `notebooks/` folder.
2. Open `train_model.ipynb` in Jupyter.
3. Prepare your own `CSV` with `source`, `destination`, `distance`, `traffic_level`, `hour`, and `travel_time`.
4. Run the notebook to generate a new `.pkl` model.
5. Replace the existing `ml/travel_time_model.pkl` with your own.

---

## 📦 Requirements

Include the following in `requirements.txt`:

```
pandas
scikit-learn
matplotlib
networkx
joblib
```

---

## 🚀 Real-World Use Cases

- Logistics and delivery companies optimizing routes
- Dynamic traffic-based rerouting systems
- Customizable route planning with real-time data

---

## 💡 Future Upgrades

- Integrate real-time traffic API (like Google Maps API)
- Web-based UI for better UX
- Multi-source delivery optimization
- Weather-aware routing

---

## ❓ FAQ

### Will the ML model train automatically after cloning?
No. The `.pkl` file is pre-trained and provided. For training your own model, use the included Jupyter notebook.

### Can I use my own data?
Yes! Use `train_model.ipynb` to train a model with your custom CSV.

---

© 2025 Logistics Route Optimizer