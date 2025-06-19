from datetime import datetime, timezone
from sqlalchemy import DateTime
from sqlalchemy.orm import mapped_column, Mapped
from src.app.core.base import Base


class Url(Base):
    __tablename__ = "urls"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    alias: Mapped[str] = mapped_column(nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)
    clicks: Mapped[int] = mapped_column(nullable=False, default=0)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    def __repr__(self):
        return f"Url(id={self.id}, alias={self.alias}, url={self.url}, clicks={self.clicks})"
