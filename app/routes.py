from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import URL

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/retrieve', methods=['GET', 'POST'])
def retrieve():
    if request.method == 'POST':
        short_url_input = request.form['short_url']
        short_url_key = short_url_input.rsplit('/', 1)[-1]
        url = URL.query.filter_by(short_url=short_url_key).first()
        if url:
            return render_template('retrieve.html', original_url=url.original_url, short_url=short_url_input)
        else:
            flash('Short URL not found. Please try again.', 'error')
    return render_template('retrieve.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        original_url = request.form['url']
        new_url = URL(original_url)
        db.session.add(new_url)
        db.session.commit()
        return render_template('create.html', short_url=new_url.short_url)
    return render_template('create.html')

@app.route('/<short_url>')
def redirect_url(short_url):
    url = URL.query.filter_by(short_url=short_url).first_or_404()
    return redirect(url.original_url)
