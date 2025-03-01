from . import bp
from flask_login import login_required, current_user, logout_user
from flask import render_template, request, abort, redirect, url_for, flash
from flask_wtf.csrf import generate_csrf, validate_csrf
from .. import db


@login_required
@bp.route('/')
def app():
    return render_template('app/app.html')


@login_required
@bp.route('/account', methods=['GET', 'POST'])
def account():
    delete_account_error = None
    csrf_token = generate_csrf()
    if request.method == 'POST':
        if not validate_csrf(request.form.get('csrf_token')):
            abort(400)
        try:
            db.session.delete(current_user)
            db.session.commit()
            logout_user()
            return redirect(url_for('main.home'))
        except Exception as e:
            db.session.rollback()
            error = 'An error occurred while deleting your account. Please try again later.', 'danger'
    return render_template('app/account.html', delete_account_error=delete_account_error)
