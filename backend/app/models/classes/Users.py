from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
import datetime
from sqlalchemy import String, Integer, DateTime
from sqlalchemy import func
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = "users"
    #relation
    ass_history_cards: Mapped[list["History_cards"]] = relationship()
    ass_get_exchange: Mapped[list["Get_Exchanges"]] = relationship(back_populates="user")
    purchases: Mapped[list["Purchases"]]= relationship(secondary= "buy",back_populates="users")

    #column
    id_user: Mapped[int] = mapped_column(primary_key=True, type_= Integer)
    last_name: Mapped[str] = mapped_column(type_= String(100), nullable=False)
    first_name: Mapped[str] = mapped_column(type_= String(100), nullable=False)
    nick_name: Mapped[str] = mapped_column(type_=String(100), nullable= False)
    date_created: Mapped[datetime.datetime] = mapped_column(type_= DateTime(timezone=True), default=func.now())
    id_wallet: Mapped[int | None] = mapped_column(type_= Integer, nullable= True, unique=True)
    date_free_pack: Mapped[datetime.datetime] = mapped_column(type_= DateTime(True), default=func.now())







