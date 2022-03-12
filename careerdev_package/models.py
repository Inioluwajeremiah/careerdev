import random
from flask_login import UserMixin
from datetime import datetime
import string

from . import db

# deadline
# application startdate
# scholarship/funding/postdoc/internship   body
#  tags




class User( UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    useremail = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now())
    date_updated = db.Column(db.DateTime, onupdate=datetime.now())

    postModel = db.relationship('PostModel', backref='user')

class PostModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ga = db.Column(db.Text, nullable=False)
    #  ra = db.Column(db.Text, nullable = True)
    title = db.Column(db.Text, nullable=False)
    subtitle = db.Column(db.Text, nullable=True)
    country = db.Column(db.Text, nullable=False)
    institution = db.Column(db.Text, nullable=False)
    faculty = db.Column(db.Text, nullable=False)
    department = db.Column(db.Text, nullable=True)
    course = db.Column(db.Text, nullable=True)
    level = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=False)
    duration = db.Column(db.Text, nullable=False)
    appfee = db.Column(db.Text, nullable=False)
    fund_type = db.Column(db.Text, nullable=False)
    fund_inst = db.Column(db.Text, nullable=False)
    app_url = db.Column(db.Text, nullable=False)
    app_short_url = db.Column(db.String(3), nullable=False)
    post_cat = db.Column(db.Text, nullable=False)
    app_sd =  db.Column(db.Text, nullable=False)
    app_ed =  db.Column(db.Text, nullable=False)
    visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now())
    date_updated = db.Column(db.DateTime, onupdate=datetime.now())
    #  waived = db.Column(db.Text, nullable = True)

    def generate_short_characters(self):
        characters = string.digits+string.ascii_letters
        picked_chars = ''.join(random.choices(characters, k=3))

        link = self.query.filter_by(app_short_url=picked_chars).first()

        if link:
            self.generate_short_characters()
        else:
            return picked_chars

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app_short_url = self.generate_short_characters()

    def __repr__(self) -> str:
        return 'PostModel>>> {self.url}'



