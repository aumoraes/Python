# test_wallet.py

import requests
import pytest

from src.wallet import Wallet
from src.insufficient_amount import InsufficientAmount
import time

@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return Wallet(20)

@pytest.fixture()
def mock_request_month_report_reponse(monkeypatch):
    class ResponseMock():
        status_code = None
    class Response:
        def request_month_report():
            response = ResponseMock()
            response.status_code = 201
            return response
        monkeypatch.setattr(requests, "get", lambda *args, **kwargs: request_month_report())
    return Response

def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance() == 0

def test_setting_initial_amount(wallet):
    assert wallet.balance() == 20

def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance() == 100

def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance() == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)

@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transactions(empty_wallet, earned, spent, expected):
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    assert empty_wallet.balance() == expected

@pytest.mark.slow
def test_wallet_request_month_report(wallet, mock_request_month_report_reponse):
    report = mock_request_month_report_reponse.request_month_report()
    
    assert report.status_code == 200, f"Teste falhou pq estava esperando 200 e retornou {report.status_code}"

@pytest.mark.slow
@pytest.mark.xfail
def test_wallet_request_day_report(wallet):
    report = wallet.request_month_report()
    
@pytest.mark.slow
def test_setting_initial_amount_with_sleep(wallet):
    
    time.sleep(1)
    assert wallet.balance() == 20