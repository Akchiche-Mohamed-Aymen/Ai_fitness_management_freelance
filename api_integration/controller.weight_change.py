from pickle import load
from pandas import read_csv,  DataFrame 
columns = read_csv('../weight_change_prediction_model/weightlifting_cleaned.csv').drop(columns=["delta_weight"]).columns
print(columns)
with open('../models/weight_change_model.pkl', 'rb') as f:
    try:
        model = load(f)
    except Exception as e:
        print(f"Error loading model: {e}")
        model = None
        exit(1) 
def predict_weight_change(input_data: dict) -> dict:
    try:
        for key in input_data:
            input_data[key] = [input_data[key]]
        input_df = DataFrame(input_data, columns=columns)
        prediction = model.predict(input_df)[0]
        prediction_proba = model.predict_proba(input_df)[0]
        return {"delta_weight": prediction, "confidence": prediction_proba}
    except Exception as e:
        print(f"Error during prediction: {e}")
        return {"error": "Prediction failed due to an internal error."}
#py controller.weight_change.py 