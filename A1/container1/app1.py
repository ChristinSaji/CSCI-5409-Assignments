from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    if not data or 'file' not in data or 'product' not in data:
        return jsonify({"file": None, "error": "Invalid JSON input."}), 400

    file_name = data['file']
    product = data['product']
    if not file_name:
        return jsonify({"file": None, "error": "Invalid JSON input."}), 400
    if not os.path.exists(f'/data/{file_name}'):
        return jsonify({"file": file_name, "error": "File not found."}), 404

    response = requests.post('http://container2:6001/sum', json=data)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
