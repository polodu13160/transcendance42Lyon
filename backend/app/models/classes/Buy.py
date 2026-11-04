from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey


class Buy(Base):
    __tablename__ = "buy"
    id_user: Mapped[int] = mapped_column(ForeignKey("users.id_user"), primary_key=True)
    id_purchase: Mapped[int] = mapped_column(ForeignKey("purchases.id_purchase"), primary_key=True)
