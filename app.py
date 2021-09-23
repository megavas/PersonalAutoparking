from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

app = Flask(__name__)

params = config()

#'postgresql://username:password@host:port/database'
app.config['SQLALCHEMY_DATABASE_URI'] = params
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)
from models.documentos import Documentos

@app.route("/")
def hello():
    doc_list = 'Tipos de documentos:<br />'
    documentos = Documentos.get_all()
    for doc in documentos:
        doc_list += doc.nombre
        doc_list += '<br />'
        
    return doc_list

@app.route("/login")
def login():
    return "Login page"

#prueba de git