from flask import render_template
from app import app, db

# Custom 404 page so users get something that matches the rest of the site.
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# On a 500 we roll back the session first - whatever broke it shouldn't linger.
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500