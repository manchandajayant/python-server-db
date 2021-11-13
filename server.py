from flask import Flask
import json

app = Flask(__name__)



@app.route("/test")
def tet():
    return {"test":json.dumps("Asdas")}

@app.route("/blue")
def b():
    return "hello"

if __name__ == "__main__":
    app.run(debug=True)
