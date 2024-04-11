from sqlalchemy import Column, ForeignKey, Integer, String, Datetime
from sqlalchemy.orm import relationship

from app.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    comments = relationship("Comments", back_populates="users")
    messages = relationship("Messages", back_populates="users")


class Messages(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(String)
    created_at = Column(Datetime)

    users = relationship("User", back_populates="messages")
    comments = relationship("Comments", back_populates="users")


class Comments(Base):
    __tablename__ = "comm"

    id = Column(Integer, primary_key=True)
    message_id = Column(Integer, ForeignKey("comm.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(String)
    created_at = Column(Datetime)

    user = relationship("User", back_populates="comm")
    comments = relationship("Comments", back_populates="comm")
