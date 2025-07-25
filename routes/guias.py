from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory, flash
from models.guia import Guia
from flask_login import login_required, current_user
import os
from datetime import timedelta
from werkzeug.utils import secure_filename

# Carpeta donde se guardan los PDF
UPLOAD_FOLDER = 'static/pdfs/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

guias_bp = Blueprint('guias', __name__)

# ------------------------
# Subir guía (protegido)
# ------------------------
@guias_bp.route('/subir', methods=['GET', 'POST'])
@login_required
def subir_guia():
    if request.method == 'POST':
        archivo = request.files.get('archivo')
        nombre = request.form.get('nombre')
        descripcion = request.form.get('descripcion')
        programa = request.form.get('programa')

        # Validación básica
        if not (archivo and nombre and descripcion and programa):
            flash("⚠️ Todos los campos son obligatorios", "danger")
            return redirect(url_for('guias.subir_guia'))

        nombre_archivo = secure_filename(archivo.filename)
        ruta = os.path.join(UPLOAD_FOLDER, nombre_archivo)
        archivo.save(ruta)

        # Guardar en base de datos
        Guia(
            nombre=nombre,
            descripcion=descripcion,
            programa=programa,
            archivo=nombre_archivo,
            instructor=current_user._get_current_object()
        ).save()

        flash("✅ Guía subida con éxito", "success")
        return redirect(url_for('guias.listar_guias'))

    return render_template('subir_guia.html')

# ------------------------
# Listar guías (público)
# ------------------------
@guias_bp.route('/listar')
def listar_guias():
    guias = Guia.objects()
    return render_template('listar_guias.html', guias=guias, timedelta=timedelta)

# ------------------------
# Descargar PDF
# ------------------------
@guias_bp.route('/pdfs/<filename>')
def descargar_pdf(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
