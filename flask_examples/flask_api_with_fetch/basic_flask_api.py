from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("basic_js_api.html")

@app.route("/students", methods=['GET'])
def get_all_students():

    students = [
        {
        "id": 1,
        "name": "Tom Smith",
        "yearGroup": "12"
    },
    {
        "id": 2,
        "name": "Mark Dark",
        "yearGroup": "13"
    }
    ]

    return json.dumps({
        "students": students,
        "status": "OK"
    })



@app.route("/student/<int:id>", methods=["GET"])
def get_student_details(id):

    students = {
        1: {
        "id": 1,
        "name": "Tom Smith",
        "yearGroup": "12"
    },
    2: {
        "id": 2,
        "name": "Mark Dark",
        "yearGroup": "13"
    }
    }

    return json.dumps(students[id])

@app.route("/student", methods=["POST"])
def post_student_details():
    data = json.loads(request.data)
    print("Data received from client...")
    print(data["name"], data["yearGroup"])
    return "", 200

app.run(debug=True)