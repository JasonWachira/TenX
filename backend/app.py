from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, County, Candidate, Donation, Expense, Party, seed_data

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campaign_finance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
db.init_app(app)

with app.app_context():
    seed_data()



if __name__ == "__main__":
    app.run(debug=True, port=5000)

