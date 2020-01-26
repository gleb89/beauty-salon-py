from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length


# CallbackForm
class CallbackForm(FlaskForm):
    user_name  = StringField('Ваше имя', validators=[InputRequired(),
                                                    Length(min=1, max=35, message='must be greater then 1 and less than 35')])
    user_phone = StringField('Номер телефона', validators=[InputRequired()])
# END CallbackForm