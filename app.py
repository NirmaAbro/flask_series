from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "hello world"

import controllers.user_controller as user_controller

if __name__ == "__main__":
    app.run(debug=True)
