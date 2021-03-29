import pytest
import requests
@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def request_month_report():
        raise RuntimeError("Network access not allowed during testing!")
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: request_month_report())

