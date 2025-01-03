 ## Comment Service
### comment-service/app.py
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

comments = {}

@app.route('/comments', methods=['POST'])
def add_comment():
    data = request.get_json()
    comment_id = len(comments) + 1
    comments[comment_id] = {
        'post_id': data['post_id'],
        'user_id': data['user_id'],
        'content': data['content'],
        'created_at': datetime.datetime.utcnow()
    }
    return jsonify({'message': f'Comment {comment_id} added successfully!'}), 201

@app.route('/comments', methods=['GET'])
def list_comments():
    post_id = request.args.get('post_id')
    post_comments = {k: v for k, v in comments.items() if v['post_id'] == int(post_id)}
    return jsonify(post_comments), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)

 
