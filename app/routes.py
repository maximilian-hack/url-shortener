from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import URL

@app.route('/create', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        new_url = URL(original_url)
        db.session.add(new_url)
        db.session.commit()
        return render_template('index.html', short_url=new_url.short_url)
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_url(short_url):
    url = URL.query.filter_by(short_url=short_url).first_or_404()
    return redirect(url.original_url)
