import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Path

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/paths")
def all_paths():
    paths = Path.query.all()
    return jsonify([e.serialize() for e in paths])


@app.route("/add-path", methods=["POST"])
def add_path():
    body = request.get_json()
    pth = Path(svg=body['svg'],
               zoom=body['zoom'],
               lat=body['lat'],
               lng=body['lng'] 
               )
    db.session.add(pth)
    db.session.commit()
    return "Path added with id {}".format(pth.id)
