from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
import datetime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import String, Integer, Numeric, DateTime, Text, BigInteger
from sqlalchemy import func
from sqlalchemy.orm import relationship



class Cards(Base):
    __tablename__= "cards"
    #relation
    ass_get_exchange: Mapped[list["Get_Exchanges"]] = relationship(back_populates="card")

    #column
    id_card: Mapped[int] = mapped_column(type_=BigInteger, primary_key=True)
    date_created: Mapped[datetime.datetime] = mapped_column(type_= DateTime(True), default=func.now())
    atk: Mapped[float] = mapped_column(Numeric(10, 2))
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