import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import User, Post

# Makes db models available in the flask shell without manual imports each time.
@app.shell_context_processor
def make_shell_context():
    return { 'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}