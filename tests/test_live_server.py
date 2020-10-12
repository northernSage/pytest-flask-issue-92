from flask import url_for
import pytest
import requests

@pytest.mark.usefixtures("live_server")
class TestLiveServer:

    @pytest.mark.usefixtures('live_server')
    def test_cookie_getting(self):
        sesh = requests.Session()
        username = 'foo'
        password = 'bar'
        response = sesh.post(
            url_for('security', _external=True),
            data={'email': username, 'password': password, 'next': None},
        )
