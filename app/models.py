from app import app
from app import db


class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32), index=True)
    last_name = db.Column(db.String(32), index=True)
    middle_name = db.Column(db.String(32), index=True)
    phone = db.Column(db.String(32), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    telegram = db.Column(db.String(32), index=True)
    vk = db.Column(db.String(64), index=True)
    gender = db.Column(db.String(20), index=True)
    city = db.Column(db.String(32), index=True)
    experience = db.Column(db.String(255), index=True)
    birthdate = db.Column(db.String(32), index=True)
    achievement = db.Column(db.String(255), index=True)
    languages = db.Column(db.String(255), index=True)
    discription = db.Column(db.String(255), index=True)
    busscard = db.relationship('Busscards', backref='user', lazy='dynamic')


class Busscards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    download_count = db.Column(db.Integer, index=True)
    contact_count = db.Column(db.Integer, index=True)
    pdf = db.Column(db.String(255), index=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))


class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, index=True)
    connection = db.Column(db.Integer, index=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))


class Qrcodes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), index=True)
    qr_image = db.Column(db.String(255), index=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))



