from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/question", methods=["GET"])
def questions():
    with open("data.json") as file:
        allData = json.load(file)
    category = request.args.get("category")
    points = request.args.get("points")

    # print(f"Category: {category}, Points: {points}")
    # print(request.args)
    # data = allData[category][points]
    data = allData[category][points]

    return render_template("question.html", question=data["question"], answer=data["answer"])