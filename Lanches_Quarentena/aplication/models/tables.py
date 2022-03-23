from aplication import db


class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Float)

    def __init__(self, nome, phone):
        self.nome = nome
        self.phone = phone

    def __repr__(self):
        return '<Cliente %r>' % self.nome


class Produto(db.Model):
    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True)
    nomeProduto = db.Column(db.String(50), nullable=False)
    valor = db.Column(db.Float)

    def __init__(self, nomeProduto, valor):
        self.nomeProduto = nomeProduto
        self.valor = valor

    def __repr__(self):
        return '<Produto %r>' % self.nomeProduto
