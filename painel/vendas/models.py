from painel import db


class Vendas(db.Model):
    __tablename__ = 'vendas'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer)
    carro = db.Column(db.String(50))
    placa = db.Column(db.String(7))
    chassi = db.Column(db.String(17))

    def __init__(self, carro, placa, chassi, cliente_id):
        self.carro = carro
        self.placa = placa
        self.chassi = chassi
        self.cliente_id = cliente_id
