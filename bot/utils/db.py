import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, ForeignKey, Text, func, select

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost:5432/proghelper")

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    telegram_id: Mapped[int] = mapped_column(Integer, unique=True, index=True)
    username: Mapped[str] = mapped_column(String(64), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

class RequestHistory(Base):
    __tablename__ = "request_history"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    request: Mapped[str] = mapped_column(Text)
    response: Mapped[str] = mapped_column(Text)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

class UserSettings(Base):
    __tablename__ = "user_settings"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), unique=True)
    model: Mapped[str] = mapped_column(String(64), default="qwen2.5:1.5b")

async def get_user_model(session: AsyncSession, telegram_id: int) -> str:
    from sqlalchemy import select
    # Получаем id пользователя по telegram_id
    result = await session.execute(select(User).where(User.telegram_id == telegram_id))
    user = result.scalar_one_or_none()
    if not user:
        return "qwen2.5:1.5b"
    db_user_id = user.id
    result = await session.execute(select(UserSettings).where(UserSettings.user_id == db_user_id))
    settings = result.scalar_one_or_none()
    return settings.model if settings else "qwen2.5:1.5b"

async def set_user_model(session: AsyncSession, user_id: int, model: str):
    # user_id здесь — telegram_id, нужно получить id из таблицы users
    result = await session.execute(select(User).where(User.telegram_id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        user = User(telegram_id=user_id)
        session.add(user)
        await session.commit()
        await session.refresh(user)
    db_user_id = user.id
    result = await session.execute(select(UserSettings).where(UserSettings.user_id == db_user_id))
    settings = result.scalar_one_or_none()
    if settings:
        settings.model = model
    else:
        settings = UserSettings(user_id=db_user_id, model=model)
        session.add(settings)
    await session.commit()

async def ensure_user_exists(session: AsyncSession, telegram_id: int, username: str = None):
    from sqlalchemy import select
    result = await session.execute(select(User).where(User.telegram_id == telegram_id))
    user = result.scalar_one_or_none()
    if not user:
        user = User(telegram_id=telegram_id, username=username)
        session.add(user)
        await session.commit()
        await session.refresh(user)
    return user

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
