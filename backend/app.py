from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
import logging

app = Flask(__name__)  # Fixed: Changed 'name' to '__name__'
CORS(app, resources={r"/api/*": {"origins": "*"}})

logging.basicConfig(level=logging.DEBUG)

try:
    client = MongoClient('mongodb://database:27017/')
    db = client['todoapp']
    todos = db.todos
    client.server_info()  # Will raise an exception if connection fails
    app.logger.info("Successfully connected to MongoDB")
except Exception as e:
    app.logger.error(f"Failed to connect to MongoDB: {e}")
    raise

@app.route('/api/todos', methods=['GET'])
def get_todos():
    try:
        return jsonify([{"id": str(todo["_id"]), "text": todo["text"]} for todo in todos.find()])
    except Exception as e:
        app.logger.error(f"Error in get_todos: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/todos', methods=['POST'])
def add_todo():
    try:
        todo = request.json
        result = todos.insert_one({"text": todo["text"]})
        return jsonify({"id": str(result.inserted_id), "text": todo["text"]})
    except Exception as e:
        app.logger.error(f"Error in add_todo: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)