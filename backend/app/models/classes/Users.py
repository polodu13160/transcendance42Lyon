from ..base import Base
from sqlalchemy.orm import Mapped, mapped_column
import datetime
from sqlalchemy import String,Integer, Numeric, DateTime, Column, ForeignKey, Table, Boolean
from sqlalchemy import func
from sqlalchemy.orm import relationship


class Buy(Base):
    __tablename__ = "buy"
    #relation and column
    id_user: Mapped[int] = mapped_column(ForeignKey("users.id_user"), primary_key=True)
    id_purchase: Mapped[int] = mapped_column(ForeignKey("purchases.id_purchase"), primary_key=True)


class History_cards(Base):
    __tablename__ = "history_cards"
    #relation
    cards: Mapped["Cards"] = relationship()

    #relation and column
    id_user: Mapped[int] = mapped_column(ForeignKey("users.id_user"), primary_key=True)
    id_card: Mapped[int] = mapped_column(ForeignKey("cards.id_card"), primary_key=True)




class Get_Exchanges(Base):
    __tablename__ = "get_and_exchanges"
    #relation
    user: Mapped["Users"] = relationship(back_populates="ass_get_exchange")
    card: Mapped["Cards"] = relationship(back_populates="ass_get_exchange")

    #column

    id_card: Mapped[int] = mapped_column(ForeignKey("cards.id_card"), primary_key=True)
    is_auction: Mapped[bool] = mapped_column(Boolean, default=False)
    id_user_auction: Mapped[int | None] = mapped_column(Integer)
    auction_bet: Mapped[int | None] = mapped_column(Integer)
    time_limit_auction: Mapped[datetime.datetime |  None ] = mapped_column(DateTime(True))
    time_created_auction: Mapped[datetime.datetime | None] = mapped_column(DateTime(True))
    time_acquisition: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    is_finish_auction: Mapped[bool] = mapped_column(Boolean, default=False)
    is_shiny: Mapped[bool] = mapped_column(Boolean, default=False)




class Rarity(Base):
    __tablename__= "rarity"
    #relation
    id_rarity: Mapped[int] = mapped_column(Integer,primary_key=True)
    colors: Mapped[str] = mapped_column(String(50))
    min_moy: Mapped[float] = mapped_column(Numeric(18,2))




class Cards(Base):
    __tablename__= "cards"
    #relation
    rarity: Mapped["Rarity"] = relationship()
    ass_get_exchange: Mapped[list["Get_Exchanges"]] = relationship(back_populates="card")
    id_rarity: Mapped[int] = mapped_column(ForeignKey("rarity.id_rarity"))

    #column
    id_card: Mapped[int] = mapped_column(type_= Integer  ,primary_key=True)
    date_created: Mapped[datetime.datetime] = mapped_column(type_= DateTime(True), default=func.now())
    nb_rating_users: Mapped[int] = mapped_column(type_= Integer)
    notation_users: Mapped[int] = mapped_column(type_ = Integer)
    notation_critics: Mapped[int] = mapped_column(type_= Integer)
    nb_rating_critics: Mapped[int] = mapped_column(type_= Integer)
    value_exchange: Mapped[int] = mapped_column(type_= Integer)
    image_url: Mapped[str] = mapped_column(type_ = String(300))
    fun_fact: Mapped[str] = mapped_column(type_= String(500))
    description: Mapped[str] = mapped_column(type_= String(500))
    urlExtern: Mapped[str] = mapped_column(type_ = String(500))
    name: Mapped[str] = mapped_column(type_ = String(500))
    name_franchise: Mapped[str] = mapped_column(type_= String(300))
    type: Mapped[str] = mapped_column(type_ = String(200))








class Purchases(Base):
    __tablename__ = "purchases"
    #relation
    users: Mapped[list["Users"]] =relationship(secondary= "buy", back_populates="purchases")

    #column
    id_purchase: Mapped[int] = mapped_column(primary_key=True, type_= Integer)
    value_crypto: Mapped[float] = mapped_column(type_= Numeric(18,2), nullable=False)
    purchase_sum: Mapped[int] = mapped_column(type_= Integer)
    qte: Mapped[int] = mapped_column(type_= Integer)

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








