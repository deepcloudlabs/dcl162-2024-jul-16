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
    jack = bank.create_customer("1", "jack bauer")
    kate = bank.create_customer("2", "kate austen")
    james = bank.create_customer("3", "james sawyer")
    mocker.patch.object(jack, "get_account", return_value=account1)
    mocker.patch.object(kate, "get_account", return_value=account2)
    mocker.patch.object(james, "get_account", return_value=account3)
    found_account = bank.get_account("tr2") #2: call exercise method
    assert found_account is not None
    assert found_account.iban == "tr1"
