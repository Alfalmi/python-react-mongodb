from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

# Instantiation
app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost/pythonreactdb"
mongo = PyMongo(app)

db = mongo.db.pythonreact

# routes
@app.route('/users', methods=['POST'])
def createUser():
    id = db.insert({
        'name': request.json['name'],
        'email': request.json['email'],
        'password': request.json['password']
    })
    return jsonify(str(ObjectId(id)))
   

@app.route('/users', methods=['GET'])
def getUsers():
    users = []
    for doc in db.find():
        users.append({
            '_id': str(ObjectId(doc['_id'])),
            'name': doc['name'],
            'email': doc['email'],
            'password': doc['password']
        })
    return jsonify(users)

@app.route('/user/<id>', methods=['GET'])
def getUser(id):
    print(id)
    return 'recieved'

@app.route('/users/<id>', methods=['DELETE'])
def deleteUser(id):
    return 'received'

@app.route('/users/<id>', methods=['PUT'])
def updateUser(id):
    return 'received'


if __name__ == "__main__":
    app.run(debug=True)