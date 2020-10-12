from flask import url_for
import pytest

def test_create_merchant(client):
    rv = client.post(
        url_for("auth"), 
        json={'username': 'flask', 'password': 'secret'}
    )
    assert rv.status_code == 200