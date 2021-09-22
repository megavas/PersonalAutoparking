from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import text

load_dotenv()

app = Flask(__name__)

#'postgresql://username:password@host:port/database'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zgnojbpnkhoqmx:5d8d7241e51758b68ce3aa6c365d746d4ea3b8a711a2b5d31c33100ef7a6705a@ec2-44-196-146-152.compute-1.amazonaws.com:5432/d26fib3rqoq9p1'
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