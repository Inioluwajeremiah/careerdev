from flask import Blueprint, request, render_template, url_for, redirect, flash
from werkzeug.security import check_password_hash, generate_password_hash
from .models import User
from flask_login import login_user, login_required, logout_user, current_user
from . import db
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        if request.form.get('login') == "Login":
            useremail = request.form.get('email')
            password = request.form.get('password')

            user = User.query.filter_by(useremail=useremail).first()

            if not user:
                flash('Useremail does not exist', category='error')
                return render_template('adminLogin.html', user=current_user, useremail=useremail)
            elif not check_password_hash(user.password, password):
                flash('Password incorrect!',category='error')
                return render_template('adminLogin.html', user=current_user, useremail=useremail)
            else:
                login_user(user, remember=True)
                flash('Login successful', category='success')
                # return render_template('main.html')
                return redirect(url_for('views.dataPage'))
        return render_template('adminLogin.html', user=current_user)

    return render_template('adminLogin.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        useremail = request.form.get('email')
        username = request.form.get('adname')
        password = request.form.get('adpass')
        cpassword = request.form.get('cadpass')
        # admin_key = request.form.get('admin_key')
        user = User.query.filter_by(username=username).first()
                
        
        if len (useremail) < 4:
            flash("Please, enter your correct email", category='error')
            return render_template('adminRegister.html', user=current_user, username = username, useremail = useremail)
        elif len (username) < 3:
            flash("Please, enter your username (at least 3 chars) ", category='error')
            return render_template('adminRegister.html', user=current_user, username = username, useremail = useremail)
        elif user:
            flash("User already exists",  category='error')
            return render_template('adminRegister.html', user=current_user,  username = username, useremail = useremail)
        elif password != cpassword:
            flash('Password does not match!', category='error')
            return render_template('adminRegister.html', user=current_user, username = username, useremail = useremail)
        # elif admin_key != 'a1178b418cae24978ed0f302c23f54ad':
        #     flash('Admin key is incorrect', category='error')
        #     return render_template('adminRegister.html', user=current_user,  username = username, useremail = useremail, admin_key = admin_key)
        else:
            #  username and password == cpassword:
            hashedPassword = generate_password_hash(password)
            adminUser = User(
                username=username, password=hashedPassword, useremail = useremail)

            db.session.add(adminUser)
            db.session.commit()
            flash('Congratulations!!! ' + username + \
                ' registration is successful, proceed to login', category='success')
            # return redirect(url_for('auth.login', success_message=success_message, user=current_user))
            return redirect(url_for('auth.login', user=current_user))
        # else:
        #     error_message = 'Password does not match!'
        #     # return redirect(request.url)
        #     return render_template('adminRegister.html', error_message=error_message, user=current_user)

    return render_template('adminRegister.html', user=current_user)
