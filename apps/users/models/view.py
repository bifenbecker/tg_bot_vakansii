import sqlalchemy as sa
from sqlalchemy.orm import relationship
from db import Base


class View(Base):
    __tablename__ = "views"

    id = sa.Column(sa.Integer, primary_key=True)
    history_id = sa.Column(sa.Integer, sa.ForeignKey("view_history.id"))
    history = relationship("ViewHistory", back_populates="views")
    view_hash = sa.Column(sa.String)
    name = sa.Column(sa.String)
