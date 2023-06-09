import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv("FLASK_SECRET_KEY") or 'prc9FWjeLYh_KsPGm0vJcg',
        SQLALCHEMY_DATABASE_URI='sqlite:///'+ os.path.join(basedir, 'globomantics.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        DEBUG=True,
        MAIL_SERVER='smtp.zoho.com',
        MAIL_PORT=465,
        MAIL_USERNAME='chrismazza@baileytech.tech',
        MAIL_PASSWORD='pv6sC6Y!tL_Jxj4',
        MAIL_USE_TLS=False,
        MAIL_USE_SSL=True

    )

    db.init_app(app)
    mail.init_app(app)
   
    from app.auth.views import auth
    from app.main.views import main
    from app.account.views import account
    from app.gig.views import gig
    from app.updateserver.views import updateserver
    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(account, url_prefix="/user")
    app.register_blueprint(gig, url_prefix="/gig")
    app.register_blueprint(updateserver)
    from app.main.errors import page_not_found
    app.register_error_handler(404, page_not_found)

    return app
