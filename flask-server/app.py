from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from model import db, Word
import json

import os
template_dir = os.path.abspath('.')
app = Flask(__name__, template_folder=template_dir)
CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"

with app.app_context():
    db.init_app(app)
    db.app = app
    db.create_all()

f = open('data.json')
data = json.load(f)

for datum in data:
    exists = db.session.query(db.exists().where(Word.value == datum['word'])).scalar()
    if exists:
        continue
    else:
        word = Word(value=datum['word'], frequency=datum['frequency'], docs=' '.join(datum['docs']), sentences=', '.join(datum['sentences']))
        db.session.add(word)
    
db.session.commit()

@app.route("/")
def my_index():
    return render_template("index.html", csrf="csrf_token")


@ app.route('/api/data', methods=['GET'])
def handle_get():
    return jsonify(Word.query.all())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
