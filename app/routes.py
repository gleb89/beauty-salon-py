from app import app
from .config import *

from flask import render_template, request, redirect, flash, url_for, send_from_directory
from flask_mail import Message

from .forms import *
from .config_mail import *


def process_callback_form(form_callback):
    user_name = form_callback.user_name.data
    user_phone = form_callback.user_phone.data

    # notification for user
    body_text = '''
        Здравствуйте, {user_name}!\n
        Вы заказали обратный звонок с сайта www.site.com, мы перезвоним вам в ближайшее время\n
        Номер телефона: {user_phone}
    '''.format(user_name=user_name, user_phone=user_phone)

    msg = Message(subject='Callback form',
                  sender='beautyroom37@mail.ru',
                  # sender='noreply@myverycustomdomain.com',
                  recipients=["beautyroom37@mail.ru"],
                  body=body_text,
                  )
    mail.send(msg)

    # notification for admin
    msg = Message(subject='Callback request',
                  sender='beautyroom37@mail.ru',
                  recipients=["beautyroom37@mail.ru"],
                  body=f'Поступила заявка на обратный звонок от {user_name}, на номер телефона: {user_phone}',
                  # html=f'<h2>Поступила заявка на обратный звонок по номеру: {user_phone}</h2><img src="https://pixlr.com/photo/image-design-11-1-pw.jpg" alt="">',
                  )
    mail.send(msg)
    flash('Успешно отправлено!', 'success')


@app.route('/', methods=['GET', 'POST'])
def homepage():
    form_callback = CallbackForm()
    if form_callback.validate_on_submit():
        process_callback_form(form_callback)
        return redirect(url_for('homepage'))

    gallery = None
    try:
        gallery = reade_content_json('app/content/gallery.json')
    except Exception as e:
        print(e)

    return render_template('pages/homepage.html', services=reade_content_json('app/content/services.json'), gallery=gallery, form_callback=form_callback)


@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_files():
    print(request.path)
    return send_from_directory(app.static_folder, request.path[1:])
