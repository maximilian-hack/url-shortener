from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import URL

# --- Admin Interface ---
@app.route('/admin', methods=['GET', 'POST'])
def admin_index():
    if request.method == 'POST':
        original_url = request.form['url']
        new_url = URL(original_url)
        db.session.add(new_url)
        db.session.commit()
        return render_template('index.html', short_url=new_url.short_url, admin=True)
    return render_template('index.html', admin=True)

# --- User Interface (No URL creation) ---
@app.route('/')
def user_index():
    return render_template('user_index.html')  # Simple page for user access

@app.route('/<short_url>')
def redirect_url(short_url):
    url = URL.query.filter_by(short_url=short_url).first_or_404()
    return redirect(url.original_url)

@app.route('/favicon.ico')
def favicon():
    return "", 204
