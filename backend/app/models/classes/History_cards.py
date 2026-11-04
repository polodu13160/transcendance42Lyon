from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship




class History_cards(Base):
    __tablename__ = "history_cards"
    #relation
    cards: Mapped["Cards"] = relationship()

    #relation and column
    id_user: Mapped[int] = mapped_column(ForeignKey("users.id_user"), primary_key=True)
    id_card: Mapped[int] = mapped_column(ForeignKey("cards.id_card"), primary_key=True)

