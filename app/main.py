from flask import Flask, request, jsonify
import pymysql
import os


app = Flask(__name__)

db_config = {
    'host': os.environ.get('MYSQL_HOST', 'localhost'),
    'user': os.environ.get('MYSQL_USER', 'default_user'),
    'password': os.environ.get('MYSQL_PASSWORD', 'default_password'),
    'database': os.environ.get('MYSQL_DATABASE', 'default_db')
}

# Connect to the database
def get_db_connection():
    return pymysql.connect(**db_config)

# Endpoint to add a name
@app.route('/add_name', methods=['POST'])
def add_name():
    name = request.json.get('name')
    if not name:
        return jsonify({"error": "Name is required"}), 400
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    try:
        cursor.execute("INSERT INTO names (name) VALUES (%s)", (name,))
        connection.commit()
        return jsonify({"message": "Name added successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

# Endpoint to list all names
@app.route('/list_names', methods=['GET'])
def list_names():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    try:
        cursor.execute("SELECT name FROM names")
        names = cursor.fetchall()
        return jsonify([name[0] for name in names]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()


if __name__ == '__main__':
    app.run(debug=True)