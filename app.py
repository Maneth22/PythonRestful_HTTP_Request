from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/process', methods=['POST'])
def process():
    data = request.form.get('data')
    # process the data using Python code
    result = data.upper()
    return result


if __name__ == '__main__':
    app.run(debug=True)