"""Configuration classes."""

from __future__ import annotations

import os


class Config:
    """Base configuration."""

    SECRET_KEY = os.getenv("SECRET_KEY", "dev")
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URL", "sqlite:///:memory:")


class DevConfig(Config):
    """Development config."""

    DEBUG = True


class ProdConfig(Config):
    """Production config."""

    DEBUG = False
