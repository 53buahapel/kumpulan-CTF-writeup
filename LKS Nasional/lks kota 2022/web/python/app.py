from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    req = request.args.get("easy", "True")
    print(req)
    eval(req, {"__builtins__": {}}, {})

    return "OK"


if __name__ == "__main__":
    app.run()
