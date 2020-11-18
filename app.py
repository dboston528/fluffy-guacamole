from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fcea0478@localhost:5432/todoapp2'
db = SQLAlchemy(app)

# this would be the model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

db.create_all()

@app.route('/todo/create', methods=['POST'])
def create_todo():
    print(request.get_json())
    formDescription = request.get_json()['description']
    todo = Todo(description=formDescription)
    db.session.add(todo)
    db.session.commit()
    return jsonify({
        'description': todo.description
    })

# this would be the controller
@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())

if __name__ == '__main__':
    app.run(debug=True)