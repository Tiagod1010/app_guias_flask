## 📚 Aplicación Web para Gestión de Guías (SENA)

Esta aplicación permite a instructores del SENA registrarse, iniciar sesión y subir guías en formato PDF a una base de datos MongoDB usando Flask y MongoEngine.

### 🚀 Funcionalidades
- Registro de instructores
- Inicio de sesión con correo y contraseña
- Subida de guías en formato PDF
- Envío de correo automático con datos de acceso
- Listado y visualización de guías
- Despliegue en Render

### 🧪 Tecnologías Usadas
- Python + Flask
- MongoDB Atlas + MongoEngine
- Flask-Login para autenticación
- Flask-Mail para notificación por correo
- Bootstrap 5 + DataTables

### 🛠️ Instalación Local
1. Clona este repositorio
```bash
git clone https://github.com/tuusuario/gestion-guias-sena.git
cd gestion-guias-sena
```

2. Crea tu archivo `.env`
```env
MONGO_URI=mongodb+srv://usuario:clave@cluster.mongodb.net/guiasDB
SECRET_KEY=clave_segura
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=tu_correo@gmail.com
MAIL_PASSWORD=clave_app
MAIL_USE_TLS=True
```

3. Instala las dependencias
```bash
pip install -r requirements.txt
```

4. Ejecuta localmente
```bash
python app.py
```

### ☁️ Despliegue en Render
1. Crea un nuevo Web Service en [Render](https://render.com)
2. Conecta tu repositorio de GitHub
3. En el `render.yaml` ya están definidos los comandos necesarios
4. Agrega las variables de entorno del `.env` en el panel de Render

---

© 2025 - Proyecto Final Python Web - SENA
