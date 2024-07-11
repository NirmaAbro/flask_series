from app import app

@app.route("/user/nirma")
def nirma():
    return "hello nirma"
