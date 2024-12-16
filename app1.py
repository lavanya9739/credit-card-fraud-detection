from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import joblib

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Load model and scaler
model = joblib.load("C:/Users/Lavanya/credit card/fraud_detection_model.pkl")
scaler = joblib.load("C:/Users/Lavanya/credit card/scaler.pkl")

# Store dataset details
dataset_path = "output_file.csv"
dataset = pd.read_csv(dataset_path)

# Home page
@app.route('/')
def home():
    return render_template("base.html")

# Page 1: Display dataset
@app.route('/dataset')
def dataset_page():
    return render_template("dataset.html", data=dataset.head(20).to_html(classes='table table-striped'))

# Page 2: Register new customers
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        customer_details = request.form
        # Handle customer registration logic (store to database or file if necessary)
        flash("Customer registered successfully!", "success")
        return redirect(url_for("register"))
    return render_template("register.html")

# Page 3: Predict fraud
@app.route('/predict', methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        form_data = request.form
        # Convert form data to a DataFrame
        input_data = pd.DataFrame([{col: form_data[col] for col in form_data}])
        
        # Preprocess input data
        input_data_scaled = scaler.transform(input_data)
        
        # Predict using the model
        prediction = model.predict(input_data_scaled)
        result = "Fraud" if prediction[0] == 1 else "Not Fraud"
        
        return render_template("predict.html", result=result)
    return render_template("predict.html")

if __name__ == "__main__":
    app.run(debug=True)
