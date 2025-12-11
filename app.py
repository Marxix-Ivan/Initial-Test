from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/readings")
def api_readings():
    return jsonify({
        "initial_tank": 63,
        "initial_P": 6.3,
        "initial_turb": 0,
        "initial_tds": 18,
        "potable_tank": 47,
        "potable_pH": 6.6,
        "potable_turb": 0,
        "potable_tds": 25
    })

@app.route("/api/predict")
def api_predict():
    return jsonify({
        "pH": 6.6,
        "Turbidity": 0,
        "TDS": 25,
        "Prediction": 1
    })

@app.route("/api/status")
def get_status():
    return jsonify([
        {"Time": "12:38", "Process": "RO Pump", "Status": "Completed"},
        {"Time": "12:31", "Process": "RO Pump", "Status": "Running"},
        {"Time": "12:24", "Process": "UV Treatment", "Status": "Running"},
        {"Time": "12:12", "Process": "Initial Filtration", "Status": "Running"},
    ])

@app.route("/api/records")
def get_records():
    return jsonify([])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
