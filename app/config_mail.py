from app import app

from flask_mail import Mail


# Mail
mail_settings = {
    "MAIL_SERVER": 'smtp.mail.ru',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'beautyroom37',
    "MAIL_PASSWORD": 'Kit241281',
}

app.config.update(mail_settings)
mail = Mail(app)
# END Mail
