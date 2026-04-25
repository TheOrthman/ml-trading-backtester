🧠 Restaurant Inventory Stockout Prediction System
📌 Overview

This project builds an end-to-end data analytics and machine learning system to monitor restaurant inventory and predict stockout risk before it happens.

The system transforms raw inventory data into actionable insights and automated predictions, enabling proactive decision-making.

🎯 Problem Statement

Restaurants often face:

Stockouts of high-demand items
Overstocking of slow-moving items
Inventory waste and cost leakage
Reactive instead of predictive restocking

This project solves that by predicting:

Will an item run out within the next 3 days?
🛠️ Tech Stack
Python
pandas
scikit-learn
Power BI (for dashboard)
SQL (for initial analysis)
🔄 Project Workflow
1. Data Processing
Cleaned and structured inventory dataset
Created key features:
days_remaining
stock_gap
2. Machine Learning Model
Model: Random Forest Classifier
Task: Binary classification (Stockout Risk)
3. Model Performance
Accuracy: 97%
Recall (after tuning): 100%
Precision: 85%

👉 Model prioritizes catching all stockout risks (business-critical)

4. Production Pipeline
Training
python src/train.py
Prediction
python src/predict.py
📂 Project Structure
.
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── predict.py
│
├── models/
│   ├── stockout_model.pkl
│   └── model_features.pkl
│
├── restaurant_inventory.csv
├── predictions.csv
├── requirements.txt
└── README.md
📊 Output

The prediction script generates:

predictions.csv

With:

stockout_risk_prediction (0 or 1)
stockout_risk_probability
💡 Key Insights
High-demand items (e.g., Milk, Eggs) are most at risk of stockouts
Overstocking contributes to waste and inefficiency
Traditional reorder logic is insufficient without demand prediction
🚀 Business Impact

This system enables:

Early detection of stockout risks
Reduced operational disruptions
Better inventory planning
Cost reduction from waste
📌 Future Improvements
Deploy as API (FastAPI)
Real-time prediction system
Automated alerts
Integration with POS/inventory systems
👤 Author

Built as part of a data analytics + machine learning portfolio project.