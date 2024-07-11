from extensions import db

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomre = db.Column(db.String(20))
    ad_soyad = db.Column(db.String(100))
    idare = db.Column(db.String(100))
    soba_xidmet = db.Column(db.String(100))
    vezife = db.Column(db.String(100))
    alternativ_nomre = db.Column(db.String(20))
    otaq_nomresi = db.Column(db.String(20))
    region = db.Column(db.String(100))
    qurum_adi = db.Column(db.String(100))
    kategoriya = db.Column(db.String(100))
    status = db.Column(db.String(20))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
