from app import db

class URL(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    longUrl=db.Column(db.String(2000),nullable=False)
    shortUrl=db.Column(db.String(15),unique=True,nullable=False)
    clickCount=db.Column(db.Integer,default=0)
    
    def __repr__(self):
        return f"<URL {self:longUrl} -> {self:shortUrl}>"
    