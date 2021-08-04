from datetime import datetime
from socialcomapnyblog import db , login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash , check_password_hash

@login_manager.user_loader
def loader(user_id):
    return user.query.get(user_id)

class user(db.Model,UserMixin):

    Id = db.Column(db.Integer,primary_key=True)
    Email = db.Column(db.String,unique=True,index=True)
    profile_pic = db.Column(db.String,nullable=False , default = 'default_pic.png')
    username = db.Column(db.String,unique=True,index=True)
    hash_pass = db.Column(db.String)

    post = db.relationship('BlogPost',backref='author')

    def __init__(self,Email,username,password):
        self.Email = Email
        self.username = username
        self.hash_pass = generate_password_hash(password)
    
    def check_pas(self,password):
        return check_password_hash(self.hash_pass,password)   


class BlogPost(db.Model, UserMixin):

    users = db.relationship(user)

    id = db.Column(db.Integer,primary_key =True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.Id'))
    date = db.Column(db.DateTime , nullable = False , default = datetime.utcnow)
    title = db.Column(db.String, nullable = False)
    Text = db.Column(db.Text , nullable = False)

    def __init__(self,title,Text,user_id):

        self.title = title
        self.Text = Text
        self.user_id = user_id

