from ..database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Book(Base):
    __tablename__ = "books"

    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str]  # по хорошему нужно сделать ForeignKey
    category: Mapped[str]  # по хорошему нужно сделать ForeignKey
    isbn: Mapped[int] = mapped_column(unique=True)
