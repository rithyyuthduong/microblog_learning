from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import loginForm


@app.route('/')
@app.route('/index')
@app.route('/login', methods=['GET', 'POST'])

def login():
    form = loginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for("index"))
    return render_template('login.html', title='Sign In', form=form)

def index():
    user = {'username': 'Rithy'}
    posts = [
        {
            'author': {'username': 'Josh'},
            'body': 'Beautiful day in Burwood!'
        },
        {
            'author': {'username': 'Mary'},
            'body': 'The movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)