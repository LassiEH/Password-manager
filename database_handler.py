from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base, relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///passdata.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    #user info
    id = Column(Integer, primary_key=True)
    username = Column("username", String, unique=True)
    email = Column("email", String)
    userpassword = Column("password", String)
    passwords = relationship('Password', back_populates='user')

    def __init__(self, username, email, userpassword):
        self.username = username
        self.email = email
        self.userpassword = userpassword

#Class that represents a stored password. The relationship is that
#every password is associated with a specific user.
class Password(Base):
    __tablename__ = "passwords"

    #password info
    id = Column(Integer, primary_key=True)
    service = Column("service", String)
    password = Column("password", String)
    username = Column("username", String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='passwords')

    #constructor
    def __init__(self, service, password, username, user=None):
        self.service = service
        self.password = password
        self.username = username
        self.user = user

Session = sessionmaker(bind=engine)
session = Session()

class UserManager:
    def create_user(username, email, password):
        new_user = User(username=username, email=email, password=password)
        session.add(new_user)
        session.commit()

    def get_user_by_credentials(username, password):
        return session.query(User).filter_by(username=username, password=password).first()
    
def hash_password(password):

    return password

Base.metadata.create_all(engine)