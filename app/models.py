from app import db
import datetime
import string
import random

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, original_url):
        self.original_url = original_url
        self.short_url = self.generate_short_url()

    def generate_short_url(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))
