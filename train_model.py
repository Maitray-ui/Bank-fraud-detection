import joblib
import pandas as pd

# Load the saved model (includes both preprocessing and classifier)
loaded_model = joblib.load("banking_app_rf.pkl")

# Example input data
data = {
    "feature1": [0.5],
    "feature2": [0.3],
    "feature3": [0.1],
    "feature4": [0.7],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Predict using the loaded model
prediction = loaded_model.predict(df)

print("Prediction:", prediction)
