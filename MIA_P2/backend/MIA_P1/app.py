from flask import Flask, jsonify, request
from flask_cors import CORS  
from readData import readData

app = Flask(__name__)
CORS(app)  

@app.route('/')
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api-execute', methods=['POST'])
def execute():
    data = request.get_json()
    entry_value = data.get('entry')
    response = readData(entry_value)
    return jsonify( {'salida': response})

if __name__ == '__main__':
    app.run(host= 'localhost',port= 8000,)
