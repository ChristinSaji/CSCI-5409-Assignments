from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

db_config = {
    'host': 'a2-rds.cc0futb4xisf.us-east-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'cloudA2june',
    'database': 'a2_rds'
}

def get_db_connection():
    return pymysql.connect(**db_config)

@app.route('/store-products', methods=['POST'])
def store_products():
    data = request.get_json()
    products = data.get('products', [])
    connection = get_db_connection()
    cursor = connection.cursor()
    for product in products:
        cursor.execute(
            "INSERT INTO products (name, price, availability) VALUES (%s, %s, %s)",
            (product['name'], product['price'], product['availability'])
        )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Success."}), 200

@app.route('/list-products', methods=['GET'])
def list_products():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT name, price, availability FROM products")
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    products_list = [{"name": row[0], "price": row[1], "availability": row[2]} for row in products]
    return jsonify({"products": products_list}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
