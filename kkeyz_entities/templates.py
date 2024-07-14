from datetime import datetime, timezone
from uuid import uuid4 as uuid

from sqlalchemy import UUID, Column, DateTime, Integer
from sqlalchemy.orm import declarative_mixin, declared_attr

@declarative_mixin
class IntegerBase:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __mapper_args__= {'always_refresh': True}

    created_at = Column(DateTime, default=datetime.now(timezone.utc), name="created_at")
    updated_at = Column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )

    id = Column("id", Integer, primary_key=True, autoincrement=True)


@declarative_mixin
class UUIDBase:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __mapper_args__= {'always_refresh': True}

    created_at = Column(DateTime, default=datetime.now(timezone.utc), name="created_at")
    updated_at = Column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )

    id = Column(
        "id", UUID, nullable=False, unique=True, primary_key=True, default=uuid()
    )

