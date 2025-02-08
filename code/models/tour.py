from app import db

class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True),
    name = db.Column(db.String(100), nullable=False),
    description = db.Column(db.String(500), nullable=False),
    price = db.Column(db.Float, nullable=False)
    # duration = db.Column(db.Integer, nullable=False),
    # image_url = db.Column(db.String(200), nullable=False),
    