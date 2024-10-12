from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import URL

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        short_url_input = request.form['short_url']
        url = URL.query.filter_by(short_url=short_url_input).first()
        if url:
            return render_template('index.html', original_url=url.original_url, short_url=short_url_input)
        else:
            flash('Short URL not found. Please try again.', 'error')
    return render_template('index.html')

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
