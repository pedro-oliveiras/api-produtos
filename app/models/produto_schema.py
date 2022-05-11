from app import ma, db
from app.models.produto import Produto


class ProdutoSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Produto
        sqla_session = db.session
        loan_instance = True

    id = ma.auto_field()
    nome = ma.auto_field()
    preco = ma.auto_field()
    quantidade = ma.auto_field()