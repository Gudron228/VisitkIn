from wtforms import SubmitField
from flask_wtf import FlaskForm


class Download(FlaskForm):
    down = SubmitField('Загрузить pdf')
