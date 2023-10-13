from flask import Flask, jsonify,request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/": {"origins": "*"}})

@app.route('/')
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'key1': 'value1', 'key2': 'value2'}
    return jsonify(data)



if __name__ == '__main__':
    app.run(port=8000)
