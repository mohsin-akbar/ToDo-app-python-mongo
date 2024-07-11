from flask import Flask, request, jsonify,redirect,render_template,url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)
app.config.from_object('config.Config')

# Initialize MongoDB client
client = MongoClient(app.config['MONGO_URI'])
db = client.todos
todo=db.todo

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        details = request.form['details']
        reminder = request.form['reminder']
        todo.insert_one({'title': title, 'details': details, 'reminder': reminder})
        all_todos = todo.find()
        return render_template('todos.html', todos=all_todos)

    all_todos = todo.find()
    return render_template('index.html', todos=all_todos)

@app.route('/todos', methods=['GET'])
def findTodos():
    all_todos = todo.find()
    return render_template('todos.html', todos=all_todos)

@app.route('/add', methods=['POST'])
def add_record():
    data = request.json
    result = db.todo.insert_one(data)
    return jsonify({'inserted_id': str(result.inserted_id)}), 201

@app.route('/<id>/delete/', methods=['POST'])
def delete(id):
    todo.delete_one({"_id": ObjectId(id)})
    all_todos = todo.find()
    return render_template('todos.html', todos=all_todos)

if __name__ == '__main__':
    app.run(debug=True)


