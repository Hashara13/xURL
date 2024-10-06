from flask import request, jsonify, redirect, render_template
from app import app, db, cache
from models import URL
import random
import string

def setUrl(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/', method=['GET', 'POST'])
def index():
    if request.method=="POST":
        
    