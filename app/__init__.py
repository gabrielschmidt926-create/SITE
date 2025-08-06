"""Application factory for Dash dashboard."""

from __future__ import annotations

import os


def create_app() -> "Dash":  # pragma: no cover - Dash not installed in tests
    """Create Dash application instance.

    Returns:
        Dash: Dash app instance.
    """
    from dash import Dash  # local import
    from flask_login import LoginManager

    server = Dash(__name__, suppress_callback_exceptions=True)
    login_manager = LoginManager()
    login_manager.init_app(server.server)

    server.title = "Fundos"
    return server
