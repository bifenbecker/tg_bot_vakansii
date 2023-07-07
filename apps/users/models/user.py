import sqlalchemy as sa
from sqlalchemy.orm import relationship
from db import Base


class User(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    telegram_id = sa.Column(sa.Integer)
    is_bot = sa.Column(sa.Boolean)
    first_name = sa.Column(sa.String)
    username = sa.Column(sa.String)
    last_name = sa.Column(sa.String)
    language_code = sa.Column(sa.String)
    is_premium = sa.Column(sa.Boolean)
    chats = relationship("Chat", back_populates="user")
    view_history = relationship("ViewHistory", back_populates="user", uselist=False)
