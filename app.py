from flask import Flask, jsonify, request, render_template, redirect
from flask_cors import CORS
import requests
app = Flask(__name__)
CORS(app)

#Starting page
@app.route('/')
def hello_world():  # put application's code here
    return render_template('form.html', value_entered=None)


# Normal Method of post (internal method)
@app.route('/demo', methods=['POST'])
def demo():
    if request.method == 'POST':
        data = request.form.get('staticEmail2')
        print(data)
        return render_template("form.html", value_entered=data)
        #return jsonify({'data': data})



#API Call And response function
@app.route('/process', methods=['POST'])
def process():
    data = request.form.get('data')
    # process the data using Python code
    result = data.upper()
    return result


if __name__ == '__main__':
    app.run(debug=True)