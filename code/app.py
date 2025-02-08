from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

from models import Tour, Booking

app = Flask(__name__)

db = SQLAlchemy(app)

app.config['SQL_ALCHEMY_URL'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'supersecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def index():
    tours = Tour.query.all()
    return render_template('index.html', tours=tours)

@app.route('/tour/<int:tour_id>', methods=['GET', 'POST'])
def tour_detail(tour_id):
    tour = Tour.query.get_or_404(tour_id)
    return render_template('tour.html', tour=tour)

@app.route('/tour/<int:tour_id>', methods=['GET', 'POST'])
def book_tour(tour_id):
    if request.method == 'POST':
        name = request.form.get['name']
        email = request.form.get['email']

        booking = Booking(tour_id=tour_id, name=name, email=email)
        db.session.add(booking)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('booking.html', tour_id=tour_id)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)