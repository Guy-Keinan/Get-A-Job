from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {"id": 1, "title": "Software Engineer", "location": "Israel", "salary": 30000},
    {"id": 2, "title": "Data Scientist", "location": "USA", "salary": 40000},
    {"id": 3, "title": "Product Manager", "location": "India", "salary": 50000},
    {"id": 4, "title": "DevOps Engineer", "location": "Canada", "salary": 60000},
]


@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def get_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True)
