# flask_endpoint.py

"""
Description:
    Creates a simple Flask endpoint which then we can use to expose outside using grok.

Author:
    Nishant Krishna

Created:
    03 October, 2022
"""

from flask import Flask, jsonify, request

# Create a Flask app which will run on http://127.0.0.1:5000/ as default
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return 'Hello, World!'


@app.route('/data', methods=['GET', 'POST'])
def endpoint():
    data = "Suspicious URL"
    return jsonify({'data': data})


# Start the app
if __name__ == '__main__':
    app.run(port=5002, debug=True)
