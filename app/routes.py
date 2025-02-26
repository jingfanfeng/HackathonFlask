from flask import Blueprint, render_template

bp = Blueprint('main', __name__)


@bp.route('/')
# ‘/’ URL is bound with hello_world() function.
def home():
    return render_template('home.html')


@bp.route('/about')
def about():
    return render_template('about.html')
