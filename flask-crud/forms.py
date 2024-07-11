from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class EntryForm(FlaskForm):
    nomre = StringField('Nömrə', validators=[DataRequired()])
    ad_soyad = StringField('Ad və Soyad', validators=[DataRequired()])
    idare = StringField('İdarə', validators=[DataRequired()])
    soba_xidmet = StringField('Şöbə Xidmət', validators=[DataRequired()])
    vezife = StringField('Vəzifə', validators=[DataRequired()])
    alternativ_nomre = StringField('Alternativ Nömrə')
    otaq_nomresi = StringField('Otaq Nömrəsi')
    region = StringField('Region', validators=[DataRequired()])
    qurum_adi = StringField('Qurum Adı', validators=[DataRequired()])
    kategoriya = StringField('Kateqoriya', validators=[DataRequired()])
    status = StringField('Status', validators=[DataRequired()])
    submit = SubmitField('Göndər')

class LoginForm(FlaskForm):
    username = StringField('İstifadəçi adı', validators=[DataRequired()])
    password = PasswordField('Şifrə', validators=[DataRequired()])
    submit = SubmitField('Daxil ol')
