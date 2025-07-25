from flask import Blueprint, render_template, redirect, request, flash, url_for
from models.instructor import Instructor
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from app import login_manager
from utils.mailer import enviar_correo

auth_bp = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(user_id):
    return Instructor.objects(id=user_id).first()

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form.get('correo')
        password = request.form.get('password')

        user = Instructor.objects(correo=correo).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('guias.subir_guia'))

        flash('Credenciales incorrectas')
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        regional = request.form.get('regional')
        usuario = request.form.get('usuario')
        password = request.form.get('password')

        if Instructor.objects(correo=correo).first():
            flash('El correo ya está registrado.')
            return redirect(url_for('auth.registro'))

        if Instructor.objects(usuario=usuario).first():
            flash('El usuario ya está en uso.')
            return redirect(url_for('auth.registro'))

        hashed_password = generate_password_hash(password)

        user = Instructor(
            nombre=nombre,
            correo=correo,
            regional=regional,
            usuario=usuario,
            password=hashed_password
        ).save()

        enviar_correo(user.correo, user.usuario, password)
        flash('Registro exitoso, revisa tu correo')
        return redirect(url_for('auth.login'))

    return render_template('register.html')