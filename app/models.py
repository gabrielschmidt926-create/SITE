"""Database models using SQLAlchemy ORM."""

from __future__ import annotations

from datetime import date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Date, ForeignKey, Integer, Numeric, String


class Base(DeclarativeBase):
    """Base class for models."""


class Administradora(Base):
    __tablename__ = "administradora"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    token: Mapped[str] = mapped_column(String, nullable=False)
    validade: Mapped[date | None] = mapped_column(Date)
    data_inicio: Mapped[date] = mapped_column(Date, nullable=False)

    fundos: Mapped[list["Fundo"]] = relationship("Fundo", back_populates="administradora")


class Fundo(Base):
    __tablename__ = "fundo"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_adm: Mapped[int] = mapped_column(ForeignKey("administradora.id"))
    nome: Mapped[str] = mapped_column(String, nullable=False)
    data_inicio: Mapped[date] = mapped_column(Date, nullable=False)

    administradora: Mapped[Administradora] = relationship("Administradora", back_populates="fundos")


class Usuario(Base):
    __tablename__ = "usuario"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    login: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    senha_hash: Mapped[str] = mapped_column(String, nullable=False)
