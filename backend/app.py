from flask import Flask, render_template, request, jsonify
import datetime
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/mark", methods=["POST"])
def mark_attendance():
    name = request.json.get("name")

    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    with open("../attendance.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, date, time])

    return jsonify({"status": "success"})

@app.route("/data")
def get_data():
    data = []
    try:
        with open("../attendance.csv", "r") as f:
            lines = f.readlines()
            for line in lines:
                entry = line.strip().split(",")
                if len(entry) == 3:
                    data.append({
                        "name": entry[0],
                        "date": entry[1],
                        "time": entry[2]
                    })
    except:
        pass

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)