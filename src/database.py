from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config import settings

async_engine = create_async_engine(settings.DATABASE_URL)


async_session = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
