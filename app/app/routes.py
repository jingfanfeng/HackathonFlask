from . import bp
from flask_login import login_required
from flask import render_template


@login_required
@bp.route('/')
def app():
    return render_template('app/app.html')


@login_required
@bp.route('/account')
def account():
    return render_template('app/account.html')
