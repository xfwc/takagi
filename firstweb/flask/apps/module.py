from firstweb.flask.apps import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app, use_native_unicode='utf8')

class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    phoneNumber = db.Column(db.String(16), unique=True)
    username = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(16), unique=True)

    @classmethod
    def login_or_not(cls, phone, password):
        result = db.session.query(Admin.password).filter_by(phoneNumber=phone).first()
        if result:
            if password == str(result[0]):
                name = str(db.session.query(Admin.username).filter_by(phoneNumber=phone).first()[0])
                return name
            else:
                return False
        else:
            return None

    @classmethod
    def register(cls, username, password, phone):
        result = db.session.query(Admin).filter_by(phoneNumber=phone).all()
        print(result)
        if result:
            return False
        p = Admin()
        p.username = username
        p.password = password
        p.phoneNumber = phone
        db.session.add(p)
        db.session.commit()
        db.session.close()
        return True





if __name__ == '__main__':
    pass
    # db.drop_all()
    # db.create_all()


