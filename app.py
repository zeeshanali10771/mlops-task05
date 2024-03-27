from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__, static_url_path="/static", static_folder="static")
app.config['MONGO_URI'] = 'mongodb://root:example@my-mongo-database:27017/userDB?authSource=admin'
mongo = PyMongo(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    if data:
        mongo.db.users.insert_one(data)
        return jsonify({'message': 'User info saved successfully'}), 200
    else:
        return jsonify({'error': 'No data received'}), 400

@app.route('/users', methods=['GET']) 
def get_users():
    users = mongo.db.users.find()
    print("users found: " , users)
    user_list = []
    for user in users:
        user_list.append({
            'username': user['username'],
            'email': user['email']
        })
    return jsonify(user_list)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081)