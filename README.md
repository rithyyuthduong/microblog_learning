# Microblog

A social blogging app built with Python and Flask, following Miguel Grinberg's [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world). Deployed and live on Render.

**Live:** [https://your-app-name.onrender.com](https://your-app-name.onrender.com)

## What it does

Users can register, write posts, follow each other, and browse a personalised feed. There's full-text search powered by Elasticsearch, password reset via email, and Gravatar-based avatars. The frontend is Bootstrap 5 and the whole thing runs on PostgreSQL in production.

## Stack

| | |
|---|---|
| Backend | Python, Flask |
| Database | SQLite (dev), PostgreSQL (prod) |
| ORM | SQLAlchemy + Flask-SQLAlchemy |
| Migrations | Flask-Migrate (Alembic) |
| Auth | Flask-Login, Werkzeug |
| Forms | Flask-WTF, WTForms |
| Search | Elasticsearch |
| Email | Flask-Mail |
| Frontend | Jinja2, Bootstrap 5 |
| Hosting | Render |

## Project structure

```
microblog/
├── app/
│   ├── auth/               # login, register, password reset
│   ├── main/               # index, profiles, search
│   ├── templates/          # Jinja2 templates
│   ├── __init__.py         # app factory
│   ├── models.py           # User, Post models
│   └── errors.py           # 404/500 handlers
├── migrations/
├── config.py
├── microblog.py
└── requirements.txt
```

## Running locally

**1. Clone and set up a virtual environment:**
```bash
git clone https://github.com/YOUR-USERNAME/microblog.git
cd microblog
python -m venv .venv

# Windows
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

**2. Install dependencies and set up the database:**
```bash
pip install -r requirements.txt
flask db upgrade
```

**3. Create a `.env` file:**
```
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db
MAIL_SERVER=smtp.googlemail.com
MAIL_PORT=587
MAIL_USE_TLS=1
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
ADMINS=your-email@gmail.com
ELASTICSEARCH_URL=http://localhost:9200
```

**4. Start the dev server:**
```bash
flask run
```

App will be at `http://localhost:5000`.

## Deployment

Hosted on Render with a managed PostgreSQL database. The `render.yaml` in this repo handles the service configuration. Required environment variables on Render:

| Variable | Value |
|---|---|
| `SECRET_KEY` | Any random secret string |
| `DATABASE_URL` | Provided automatically by Render Postgres |
| `FLASK_APP` | `microblog` |
| `ADMINS` | Your email address |

## What I learned

This project was my main way of getting comfortable with Flask beyond simple tutorials. The parts that took the most work were the follower system (many-to-many self-referential relationship), wiring up JWT-based password reset tokens, and getting Elasticsearch to stay in sync with the database. Deploying to Render with PostgreSQL also taught me a lot about production config vs development config — things like `DATABASE_URL` formats, `psycopg2-binary`, and why environment variables matter.

## Acknowledgements

Based on the [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by Miguel Grinberg.

## Author

**YOUR FULL NAME**
- GitHub: [@rithyyuthduong](https://github.com/rithyyuthduong)
- LinkedIn: [Rithy Yuth Duong](https://www.linkedin.com/in/rithy-yuth-duong-5021b3379/)
