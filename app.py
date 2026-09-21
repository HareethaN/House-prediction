from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model once when server starts
model = joblib.load("model_joblib.pkl")

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "API is running"
    })

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    input_df = pd.DataFrame([{
        "income": data["income"],
        "creditscore": data["credit_score"],
        "_employment_type": data["employment_type"],
        "region": data["region"]
    }])

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    return jsonify({
        "prediction": "Approve" if prediction == 1 else "Reject",
        "probability": round(float(probability), 3)
    })

if __name__ == "__main__":
    app.run(debug=True)