from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String, nullable=False)

    def __repr__(self):
        return "<User: {}>".format(self.name)

class Tweet(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))
    vect = DB.Column(DB.PickleType, nullable=False)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey("user.id"),nullable=False)
    user = DB.relationship("User", backref=DB.backref("tweets", lazy=True))

    def __repr__(self):
        return "<Tweet: {}>".format(self.text)

def insert_data():
    Rafy= User(id=2, name="Rafy")
    Arm = User(id=3, name="Armandina")
    Yera = User(id=14, name="Yeraldina")
    Alesa = User(id=22, name="Alessandra")
    
    DB.session.add(Rafy)
    DB.session.add(Arm)
    DB.session.add(Yera)
    DB.session.add(Alesa)
    DB.session.commit()
