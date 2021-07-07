from services.serve import db

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"nama {self.name} age {self.age} years old"

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
