from app import db

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True),
    tour_id = db.Column(db.Integer, db.ForeignKey('tour.id'), nullable=False),
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False),
    date_booked = db.Column(db.Date, nullable=False),
    quantity = db.Column(db.Integer, nullable=False),
    email = db.Column(db.String(255), nullable=False)

