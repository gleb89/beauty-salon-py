from app import app

from flask_mail import Mail


# Mail
mail_settings = {
    "MAIL_SERVER": 'smtp.mail.ru',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'beautyroom37@mail.ru',
    "MAIL_PASSWORD": 'Kit241281',
    "MAIL_DEFAULT_SENDER": 'beautyroom37@mail.ru'
}

app.config.update(mail_settings)
mail = Mail(app)
# END Mail
