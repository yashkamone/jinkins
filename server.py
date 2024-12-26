from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return "flask application version 1.0"

app.run(host="0.0.0.0", port=4000)