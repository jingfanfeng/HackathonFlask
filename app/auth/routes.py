from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import bp
from ..models import User
from .. import db
from .forms import LoginForm, SignupForm
from sqlalchemy.exc import IntegrityError


@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('app.app'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('app.app'))
        flash('Invalid email or password.', 'danger')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'{error}', 'danger')
    return render_template('auth/signin.html', form=form)


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        # Create and add user
        try:
            new_user = User(email=form.email.data)
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)  # Login the new user automatically
            return redirect(url_for('app.app'))
        except IntegrityError as e:
            # Database error; most likely because account with the email address already exists
            db.session.rollback()
            print(f'An error occurred: {e}')
            flash(
                'Email address is already registered. Please use a different email address or sign in.', 'danger')
        except Exception as e:
            db.session.rollback()
            flash(
                'An unexpected error occurred during registration. Please try again later.', 'danger')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'{error}', 'danger')
    return render_template('auth/signup.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))
