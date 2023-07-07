import sqlalchemy as sa
from sqlalchemy.orm import relationship
from db import Base


class ViewHistory(Base):
    __tablename__ = "view_history"

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    user = relationship("User", back_populates="view_history")
    views = relationship("View", back_populates="history")
