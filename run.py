from app import app, db

# Ensure the app context is available when creating the database
with app.app_context():
    db.create_all()  # Create the database on first run