from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from config import settings
from sqlalchemy.orm import sessionmaker
import warnings
from sqlalchemy import exc as sa_exc

warnings.simplefilter("ignore", category=sa_exc.SAWarning)

engine = create_async_engine(
    "mysql+asyncmy://flaskusr:flaskpass@db/flaskdb?charset=utf8mb4"
    )

async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

metadata = MetaData()
Base = declarative_base(metadata=metadata)


async def get_async_session():
    db = async_session()
    try:
        yield db
    finally:
        await db.close()