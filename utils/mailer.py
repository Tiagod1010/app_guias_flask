from flask_mail import Message
from app import mail
from flask import current_app

def enviar_correo(destinatario, usuario, contrasena):
    with current_app.app_context():
        msg = Message("✅ Registro exitoso en la plataforma de guías",
                      sender=current_app.config['MAIL_USERNAME'],
                      recipients=[destinatario])
        msg.body = f"""
¡Hola!

Tu registro ha sido exitoso en la plataforma de instructores del SENA.

🔐 Tus credenciales son:
📧 Usuario: {usuario}
🔑 Contraseña: {contrasena}

Puedes iniciar sesión en el siguiente enlace:
http://localhost:5000/login

¡Gracias por usar nuestra plataforma!
        """
        mail.send(msg)
