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
│   └── traffic_data.csv                # Source/destination pairs with distance & travel info (source,target,distance,time_of_day,traffic_level,travel_time
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

## 📊 Algorithms and Libraries Used

- Dijkstra's Algorithm – For shortest path optimization

- Random Forest Regression – For travel time prediction

- Pandas, NetworkX, Matplotlib – For data handling and visualization

---

## 🔍 How It Works

1. **Input**  
   - Source city and destination city  
   - Time of day and traffic level 
   - Inputs are to be given in `csi.py` after running it

2. **Graph Setup**  
   - Reads a CSV file to construct a directed graph  
   - Each edge represents a possible route between two locations

3. **Prediction**  
   - For each edge `(u, v)`:
     - Distance is read from the CSV  
     - Time of day and traffic level are passed to `predictor.py`  
     - A pre-trained ML model (`.pkl` file) predicts travel time → this becomes the edge weight

4. **Optimization**  
   - Dijkstra’s algorithm is used to find the path with the least total predicted travel time

5. **Output**  
   - Displays the optimized route  
   - graph aswell if selected

---

## 📂 What Each File Does

| File                         | Purpose                                                  |
|------------------------------|----------------------------------------------------------|
| `src/cli.py`                 | Main user interface, collects inputs, calls route logic  |
| `src/dijkstra.py`            | Custom Dijkstra with ML-adjusted weights                 |
| `src/predictor.py`           | Preprocesses input and calls ML `.predict()`             |
| `src/visualize_route.py`     | Visualizes the optimized route                           |
| `ml/travel_time_model.pkl`   | Trained `RandomForestRegressor` model                    |
| `notebooks/train_model.ipynb`| Custom graph creation and model training                 |
| `data/traffic_data.csv`      | Traffic data                                             |


---

## 💻 How to Use

### 1. Clone the repository
```bash
git clone https://github.com/chaitanya-mutyala/Logistics-Route-Optimizer.git
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


---

## 📊 Train with Your Own Data

1. Go to the `notebooks/` folder.
2. Open `train_model.ipynb` in Jupyter.
3. Prepare your own `CSV` with `source`, `destination`, `distance`, `traffic_level`, `hour`, and `travel_time`.
4. Run the notebook to generate a new `.pkl` model.
5. Replacing the existing `ml/travel_time_model.pkl` with your own.

---

## 🚀 Real-World Use Cases

- Logistics and delivery companies optimizing routes
- Dynamic traffic-based rerouting systems
- Customizable route planning with real-time data

---

## 💡 Future Upgrades

- 🔄 Integrate with real-time traffic APIs like Google Maps or OpenStreetMap
- 🧭 Web-based UI (Flask or Streamlit)
- 🗺️ Multi-route / multi-agent simulation
- 📉 Use live telemetry data for continuous ML model retraining
- 🧾 Store route history and performance analytics

---

## 🤝 Contributing

- PRs welcome! For suggestions, bug reports, or ideas, open an issue.

---

## 👨‍💻 Author

- Made with ❤️ for portfolio & learning.

---
