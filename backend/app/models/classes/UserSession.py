from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
import datetime
from sqlalchemy import ForeignKey



class UserSession(Base):
    __tablename__ = "sessions"
    id: Mapped[int] = mapped_column(primary_key=True)
    token_hash: Mapped[str] = mapped_column(unique=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    expires_at: Mapped[datetime]