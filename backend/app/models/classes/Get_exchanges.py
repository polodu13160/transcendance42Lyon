from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
import datetime
from sqlalchemy import Integer, DateTime, ForeignKey, Boolean, String
from sqlalchemy.orm import relationship



class Get_Exchanges(Base):
    __tablename__ = "get_and_exchanges"
    #relation
    user: Mapped["Users"] = relationship(back_populates="ass_get_exchange")
    card: Mapped["Cards"] = relationship(back_populates="ass_get_exchange")

    #column

    id_card: Mapped[int] = mapped_column(ForeignKey("cards.id_card"), primary_key = True)
    id_user: Mapped[int] = mapped_column(ForeignKey("users.id_user"), nullable = False)
    collection_name: Mapped[str | None] = mapped_column(String((200)), nullable = True)
    is_auction: Mapped[bool] = mapped_column(Boolean, default=False)
    is_favorite: Mapped[bool] = mapped_column(Boolean, default=False)
    id_user_auction: Mapped[int | None] = mapped_column(Integer)
    auction_bet: Mapped[int | None] = mapped_column(Integer)
    time_limit_auction: Mapped[datetime.datetime |  None ] = mapped_column(DateTime(True))
    time_created_auction: Mapped[datetime.datetime | None] = mapped_column(DateTime(True))
    time_acquisition: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    is_finish_auction: Mapped[bool] = mapped_column(Boolean, default=False)
    is_shiny: Mapped[bool] = mapped_column(Boolean, default=False)
