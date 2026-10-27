from ..base import Base
from sqlalchemy.orm import Mapped, mapped_column
import datetime
from sqlalchemy.dialects.postgresql import JSONB
import enum
from sqlalchemy import String,Integer, Numeric, DateTime, Column, ForeignKey, Table, Boolean, BigInteger, Text, Enum
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
    id_user: Mapped[int] = mapped_column(ForeignKey("users.id_user"), nullable=False)
    is_auction: Mapped[bool] = mapped_column(Boolean, default=False)
    id_user_auction: Mapped[int | None] = mapped_column(Integer)
    auction_bet: Mapped[int | None] = mapped_column(Integer)
    time_limit_auction: Mapped[datetime.datetime |  None ] = mapped_column(DateTime(True))
    time_created_auction: Mapped[datetime.datetime | None] = mapped_column(DateTime(True))
    time_acquisition: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    is_finish_auction: Mapped[bool] = mapped_column(Boolean, default=False)
    is_shiny: Mapped[bool] = mapped_column(Boolean, default=False)



class Colors(enum.Enum):
    GREY = 50
    BLUE = 80
    PURPLE = 95
    GOLD = 100


class Cards(Base):
    __tablename__= "cards"
    #relation
    ass_get_exchange: Mapped[list["Get_Exchanges"]] = relationship(back_populates="card")

    #column
    id_card: Mapped[int] = mapped_column(type_= Integer  ,primary_key=True)
    date_created: Mapped[datetime.datetime] = mapped_column(type_= DateTime(True), default=func.now())
    attq: Mapped[float] = mapped_column(Numeric(10, 2))
    def_: Mapped[float] = mapped_column(Numeric(10, 2))
    value_exchange: Mapped[int] = mapped_column(type_= Integer)
    covers_urls: Mapped[list[str]] = mapped_column(JSONB)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    urlExtern: Mapped[list[str] | None] = mapped_column(JSONB, nullable=True)
    urlIgdb: Mapped[str | None] = mapped_column(type_= String(500), nullable=True)
    name: Mapped[str] = mapped_column(type_ = String(500))
    name_franchise: Mapped[str | None] = mapped_column(type_= String(300), nullable=True)
    game_type: Mapped[int] = mapped_column(Integer)
    colors: Mapped[int | None] = mapped_column(type_ = Integer, nullable=True)
    parent_game_id: Mapped[int | None] = mapped_column(type_= Integer, nullable=True)
    genre: Mapped[list[str] | None] = mapped_column(type_=JSONB, nullable=True)
    company_game: Mapped[list[str] | None] = mapped_column(type_= JSONB, nullable=True)
    

class Wrapper(Base):
    __tablename__ = "wrapper"

    # key
    id_igdb: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    # obligatory Data
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    game_type: Mapped[int] = mapped_column(Integer, nullable=False)

    # Data
    cover_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    url: Mapped[str | None] = mapped_column(String(255), nullable=True)
    version_title: Mapped[str | None] = mapped_column(String(255), nullable=True)
    franchise_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    dlcs_parent_game_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True)

    # Notation
    aggregated_rating: Mapped[float | None] = mapped_column(Numeric(5, 2), nullable=True)
    aggregated_rating_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    rating: Mapped[float | None] = mapped_column(Numeric(5, 2), nullable=True)
    rating_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    total_rating: Mapped[float | None] = mapped_column(Numeric(5, 2), nullable=True)
    total_rating_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    hypes: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # Text
    summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    storyline: Mapped[str | None] = mapped_column(Text, nullable=True)

    # json 
    genres_name: Mapped[list[dict[str]] | None] = mapped_column(JSONB, nullable=True)
    themes_name: Mapped[list[dict[str]] | None] = mapped_column(JSONB, nullable=True)
    artworks_url: Mapped[list[dict[str]] | None] = mapped_column(JSONB, nullable=True)
    websites_url: Mapped[list[dict[str]] | None] = mapped_column(JSONB, nullable=True)
    collections_name: Mapped[list[dict[str]] | None] = mapped_column(JSONB, nullable=True)
    involved_companies_company_name: Mapped[list[dict[str]] | None] = mapped_column(JSONB, nullable=True)
    bayesian: Mapped[float] = mapped_column(Numeric(5, 2), nullable=True)



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
    date_free_pack: Mapped[datetime.datetime] = mapped_column(type_= DateTime(True), default=func.now())







