# Deployable Multi-Service Blog Application Using Docker and AWS

## User Service
### user-service/app.py

from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

users = {}

# Authentication decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = users.get(data['username'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if username in users:
        return jsonify({'message': 'User already exists!'}), 400
    users[username] = generate_password_hash(password)
    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if username not in users or not check_password_hash(users[username], password):
        return jsonify({'message': 'Invalid credentials!'}), 401
    token = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'], algorithm="HS256")
    return jsonify({'token': token})

@app.route('/users/<id>', methods=['GET', 'PUT', 'DELETE'])
@token_required
def user_operations(current_user, id):
    if request.method == 'GET':
        return jsonify({'user': current_user})
    elif request.method == 'PUT':
        return jsonify({'message': f'User {id} updated successfully!'}), 200
    elif request.method == 'DELETE':
        return jsonify({'message': f'User {id} deleted successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

 
