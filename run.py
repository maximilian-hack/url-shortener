from app import app, db

# Admin app instance
def create_admin_app():
    admin_app = app
    return admin_app

# User app instance
def create_user_app():
    user_app = app
    return user_app

if __name__ == '__main__':
    # Admin app on port 5000
    from threading import Thread
    def run_admin():
        with app.app_context():
            db.create_all()  # Ensure the database is set up
        admin_app = create_admin_app()
        admin_app.run(debug=True, port=5000, host='0.0.0.0')

    # User app on port 8080
    def run_user():
        user_app = create_user_app()
        user_app.run(debug=True, port=8080, host='0.0.0.0')

    # Run both apps on different threads
    admin_thread = Thread(target=run_admin)
    user_thread = Thread(target=run_user)
    admin_thread.start()
    user_thread.start()
    admin_thread.join()
    user_thread.join()
