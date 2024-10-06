from app import db

class URL(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    longUrl=db.Column(db.String(2000),nullable=False)
    