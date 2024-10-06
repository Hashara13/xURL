from flask import request, jsonify, redirect, render_template
from xURL import app, db, cache 
from app import app, db, cache
from models import URL
import random
import string

def setUrl(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/', method=['GET', 'POST'])
def index():
    if request.method=="POST":
        longUrl=request.form(longUrl)
        shortUrl=setUrl()
        newUrl=URL(longUrl=longUrl,shortUrl=shortUrl)
        db.session.add(newUrl)
        db.session.commit()
        
        return jsonify({'shortUrl':request.host_url+shortUrl})
    return render_template('index.html')

@app.route('<shortUrl>')
def returnUrl(shortUrl):
    url=URL.query.filter_by(shortUrl=shortUrl).first_or_404()
    url.clickCount=1
    db.session.commit()
    return redirect(url.longUrl)

@app.route('count/<shortUrl>')
def countClick(shortUrl):
    url=URL.query.filter_by(shortUrl=shortUrl).first_or_404()
    return jsonify({'shortUrl': url.shortUrl, 'clickCount': url.clickCount})

    
        
    