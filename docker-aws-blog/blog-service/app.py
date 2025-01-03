## Blog Service
### blog-service/app.py

from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

blogs = {}

@app.route('/blogs', methods=['POST'])
def create_blog():
    data = request.get_json()
    blog_id = len(blogs) + 1
    blogs[blog_id] = {
        'title': data['title'],
        'content': data['content'],
        'author_id': data['author_id'],
        'created_at': datetime.datetime.utcnow()
    }
    return jsonify({'message': f'Blog {blog_id} created successfully!'}), 201

@app.route('/blogs', methods=['GET'])
def list_blogs():
    return jsonify(blogs), 200

@app.route('/blogs/<id>', methods=['GET', 'PUT', 'DELETE'])
def blog_operations(id):
    id = int(id)
    if id not in blogs:
        return jsonify({'message': 'Blog not found!'}), 404
    if request.method == 'GET':
        return jsonify(blogs[id]), 200
    elif request.method == 'PUT':
        data = request.get_json()
        blogs[id].update(data)
        return jsonify({'message': f'Blog {id} updated successfully!'}), 200
    elif request.method == 'DELETE':
        blogs.pop(id)
        return jsonify({'message': f'Blog {id} deleted successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
