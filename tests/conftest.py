from app import create_app
import pytest
from flask import Response

@pytest.fixture(scope='session')
def app():
    app = create_app()
    return app
