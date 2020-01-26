from flask import Flask

app = Flask(__name__)
app.secret_key = 'fdkmglkndfblnvbnkjdfnbjndfljbnfbkjnnmfdnbmf'

from .config_mail import *
from .context_processors import *
from .routes import *