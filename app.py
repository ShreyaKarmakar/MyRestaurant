from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Welcome to home page!!! SHREYA"

if __name__ == '__main__':
    app.run(port=5000)