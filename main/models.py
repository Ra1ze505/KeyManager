from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import relationship, scoped_session
from sqlalchemy.ext.declarative import declarative_base

try:
    from settings import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
except ImportError:
    from main.settings import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME



Base = declarative_base()
engine = create_engine(f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}', echo=True)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, unique=True)
    key = relationship("UserKey", back_populates="user")


class UserKey(Base):
    __tablename__ = 'key'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.chat_id'))
    user = relationship("User", back_populates="key")

    title = Column(String(255))
    login = Column(String(255))
    password = Column(String(255))



