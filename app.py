import os
from flask import Flask
from uuid import UUID

app= Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

@app.route("/about")
def about():
    return "I am Waqar Iftekhar"


@app.route("/users")
def users():
    return "Welcome to User Page"

@app.route("/user/<name>")    
def user(name):
    return f"Hello {name}"

@app.route("/student/<name>/<course>/<int:id>")
def student(name,course,id):
    return f"Hello {name} is learning {course} and his id is {id}"

@app.route("/files/<path:file_path>")    
def files(file_path):
    return file_path

@app.route("/loser/<uuid:user_id>")    
def loser(user_id):
    return str(user_id)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)