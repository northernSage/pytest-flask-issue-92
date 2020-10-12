from app import create_app
import pytest

@pytest.fixture(scope='session')
def app():
    app = create_app()
    return app