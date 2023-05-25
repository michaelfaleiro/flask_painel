from painel import db, app
from painel.auth.models import User

with app.app_context():
    db.create_all()
