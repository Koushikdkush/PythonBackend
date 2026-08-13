import uuid
from sqlalchemy import Integer, String, UUID, Float, Column
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class Products(Base):
    __tablename__ = "products"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    productName: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column(Float)
    description = Column(String(300), nullable=True)
    stock = Column(Integer, nullable=True)

