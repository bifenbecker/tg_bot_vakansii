import sqlalchemy as sa
from sqlalchemy.orm import relationship
from db import Base


class Chat(Base):
    __tablename__ = "chats"

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.ForeignKey("users.id"))
    user = relationship("User", back_populates="chats")
    type = sa.Column(sa.String)
    title = sa.Column(sa.String)
    description = sa.Column(sa.String)
    location = sa.Column(sa.String)
    invite_link = sa.Column(sa.String)
