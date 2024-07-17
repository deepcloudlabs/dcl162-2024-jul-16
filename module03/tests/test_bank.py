import pytest

from banking.account import Account, AccountStatus
from banking.bank import Bank
from banking.customer import Customer

banks = [
    ("garanti"),
    ("isbankasi"),
    ("denizbank")
]


@pytest.fixture
def a_bank():
    bank = Bank("isbankasi")
    bank.create_customer("1", "jack bauer")
    bank.create_customer("2", "kate austen")
    bank.create_customer("3", "james sawyer")
    return bank


@pytest.mark.parametrize("name", banks)
def test_create_customer_is_successful(name):
    bank = Bank(name)
    assert bank.name == name
    assert len(bank.customers) == 0


def test_get_account_should_success(mocker):
    bank = Bank("isbankasi")
    account1 = Account("tr1", 10_000, AccountStatus.ACTIVE)
    account2 = Account("tr2", 20_000, AccountStatus.ACTIVE)
    account3 = Account("tr3", 30_000, AccountStatus.ACTIVE)
    account4 = Account("tr4", 40_000, AccountStatus.ACTIVE)
    account5 = Account("tr5", 50_000, AccountStatus.ACTIVE)
    account6 = Account("tr6", 60_000, AccountStatus.ACTIVE)
    accounts1 = {
        "tr1": account1,
        "tr2": account2,
        "tr3": None,
        "tr4": None,
        "tr5": None,
        "tr6": None
    }
    accounts2 = {
        "tr1": None,
        "tr2": None,
        "tr3": account3,
        "tr4": account4,
        "tr5": None,
        "tr6": None
    }
    accounts3 = {
        "tr1": None,
        "tr2": None,
        "tr3": None,
        "tr4": None,
        "tr5": account5,
        "tr6": account6
    }
    jack = bank.create_customer("1", "jack bauer")
    kate = bank.create_customer("2", "kate austen")
    james = bank.create_customer("3", "james sawyer")
    mocker.patch.object(jack, "get_account", side_effect=lambda iban: accounts1[iban])
    mocker.patch.object(kate, "get_account", side_effect=lambda iban: accounts2[iban])
    mocker.patch.object(james, "get_account", side_effect=lambda iban: accounts3[iban])
    found_account = bank.get_account("tr4")  # 2: call exercise method
    assert found_account is not None
    assert found_account.iban == "tr4"
    assert found_account == account4
