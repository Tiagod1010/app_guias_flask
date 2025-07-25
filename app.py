from flask import Flask
from flask_mail import Mail
from flask_login import LoginManager
from mongoengine import connect
from config import Config

mail = Mail()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    connect(host=app.config['MONGODB_SETTINGS']['host'])
    mail.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    from models.instructor import Instructor
    
    @login_manager.user_loader
    def load_user(user_id):
        return Instructor.objects(id=user_id).first()
    
    from routes.auth import auth_bp
    from routes.main import main_bp
    from routes.guias import guias_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(guias_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)