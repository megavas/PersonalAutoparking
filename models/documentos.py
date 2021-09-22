from app import database

class Documentos(database.Model):
    __tablename__ = 'documentos'
    
    id_d = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String, nullable=False)
    

    @staticmethod
    def get_all():
        return Documentos.query.all()