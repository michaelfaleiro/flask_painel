from painel import db


class Vendas(db.Model):
    __tablename__ = 'vendas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    carro = db.Column(db.String(50))
    placa = db.Column(db.String(8))
    chassi = db.Column(db.String(17))
    produtos = db.relationship(
        'Produtos_Vendas', backref='produtos_venda', lazy=True)

    def __init__(self, carro, placa, chassi, nome):
        self.carro = carro
        self.placa = placa
        self.chassi = chassi
        self.nome = nome


class Produtos_Vendas(db.Model):
    __tablename__ = 'produtos_vendas'
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(50))
    quantidade = db.Column(db.Integer, default=1)
    produto = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Double(8.2), default=0)
    id_venda = db.Column(db.Integer, db.ForeignKey('vendas.id'))

    def __init__(self, quantidade, produto, sku, preco, id_venda):
        self.quantidade = quantidade
        self.sku = sku
        self.produto = produto
        self.preco = preco
        self.id_venda = id_venda
