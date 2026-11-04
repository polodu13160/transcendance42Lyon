from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import String, Integer, Numeric, BigInteger, Text



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
