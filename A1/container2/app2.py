from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum_product():
    data = request.get_json()
    file_name = data['file']
    product = data['product']
    
    try:
        total = 0
        with open(f'/data/{file_name}', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['product'] == product:
                    total += int(row['amount'])
        return jsonify({"file": file_name, "sum": total})
    except Exception as e:
        return jsonify({"file": file_name, "error": "Input file not in CSV format."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001)
