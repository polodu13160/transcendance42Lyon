from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Numeric, DateTime, func, BigInteger
from sqlalchemy.orm import relationship
import datetime



class Purchases(Base):
    __tablename__ = "purchases"
    #relation
    users: Mapped[list["Users"]] = relationship(secondary= "buy", back_populates= "purchases")

    #column
    id_purchase: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    value_crypto: Mapped[float] = mapped_column(type_= Numeric(18,2), nullable=False)
    purchase_sum: Mapped[int] = mapped_column(type_= Integer)
    qte: Mapped[int] = mapped_column(type_= Integer)
    date: Mapped[datetime.datetime] = mapped_column(type_= DateTime(True), default=func.now())
