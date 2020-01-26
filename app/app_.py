import datetime
from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length


app = Flask(__name__)
app.secret_key = 'fdkmglkndfblnvbnkjdfnbjndfljbnfbkjnnmfdnbmf'


# Mail
mail_settings = {
    "MAIL_SERVER": 'smtp.mail.ru',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'testmail20211',
    "MAIL_PASSWORD": '123456w1',
}

app.config.update(mail_settings)
mail = Mail(app)
# END Mail


# CallbackForm
class CallbackForm(FlaskForm):
    # user_name  = StringField('Ваше имя', validators=[InputRequired(message='Required!!!'), Length(min=6, max=35])
    user_name  = StringField('Ваше имя', validators=[InputRequired(), Length(min=6, max=35, message='must be greater then 6 and less than 35')])
    user_phone = StringField('Номер телефона', validators=[InputRequired()])
# END CallbackForm


@app.context_processor
def template_functions():
    return dict(
        current_year=datetime.datetime.now().year,
    )
    # return {
    #     'current_year': datetime.datetime.now().year,
    # }

@app.context_processor
def site_settings():
    return dict(
        site_phone='+79991845015',
        site_phone_formated='+7 999 184-50-15',
        site_email='glebhleb89@icloud.com',
        site_address='г. Камышин, ул. Терешковой 10',
        site_social=[
            {'name': 'ВКонтакте', 'url': 'https://vk.com'},
            {'name': 'Instagram', 'url': 'https://instagram.com'},
            {'name': 'Facebook', 'url': 'https://facebook.com'},
            {'name': 'YouTube', 'url': 'https://youtube.com'},
        ],
        site_schedule='<div>Пн-Пт c 9:00 до 18:00</div> \
                        <div>Cб-Вс c 9:00 до 17:00</div>',
        site_map='<script type="text/javascript" charset="utf-8" async src="https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3A2a445e6b23d49f1064dbe1661cc02642fcf2d26ceb58128b29dd10e48ede002d&amp;width=100%25&amp;height=400&amp;lang=ru_RU&amp;scroll=false"></script>',
    )


@app.route('/', methods=['GET', 'POST'])
def homepage():
    form_callback = CallbackForm()

    if form_callback.validate_on_submit():
        # pass
        return redirect(url_for('homepage'))

    return render_template('pages/homepage.html', form_callback=form_callback)


@app.route('/callback-form', methods=['POST'])
def callback_form():
    if request.method == 'POST':
        user_name = request.form.get('user-name')
        user_phone = request.form.get('user-phone')

        if not user_name and user_phone:
            flash('Имя не может быть пустым', 'danger')

        if not user_phone and user_name:
            flash('Укажите пожалуйста свой телефон', 'danger')

        if not user_name and not user_phone:
            flash('Заполните все поля', 'danger')

        if user_name and user_phone:
            # notification for user
            body_text = '''
                Здравствуйте, {user_name}!\n
                Вы заказали обратный звонок с сайта www.site.com, мы перезвоним вам в ближайшее время\n
                Номер телефона: {user_phone}
            '''.format(user_name=user_name, user_phone=user_phone)

            msg = Message(subject='Callback form',
                            sender='testmail20211@mail.ru',
                            # sender='noreply@myverycustomdomain.com',
                            recipients=["pefylftk@grr.la"],
                            body=body_text,
                        )
            mail.send(msg)

            # notification for admin
            msg = Message(subject='Callback request',
                            sender='testmail20211@mail.ru',
                            recipients=["testmail20211@mail.ru"],
                            # body=f'Поступила заявка на обратный звонок по номеру: {user_phone}',
                            html=f'<h2>Поступила заявка на обратный звонок по номеру: {user_phone}</h2><img src="https://pixlr.com/photo/image-design-11-1-pw.jpg" alt="">',
                        )
            mail.send(msg)

            flash('Успешно отправлено!', 'success')

        return redirect(url_for('homepage'))