from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__= "tb_user"
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(24), unique=True, nullable=False)
    password=db.Column(db.Text(), nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.now())
    updated_at=db.Column(db.DateTime, onupdate=datetime.now())
    
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password, method="sha256")
        
    def __str__(self):
        return f"<User(id={self.id}, username={self.username}, created_at={self.created_at}, updated_at={self.updated_at})>"
    
    def verify_password(self, password):
        return check_password_hash(self.password, password)
