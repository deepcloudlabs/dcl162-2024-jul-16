import pytest

from banking.account import Account, AccountStatus
from banking.customer import Customer

customers = [
    ("1", "kate austen"),
    ("2", "james sawyer"),
    ("3", "ben linus")
]


@pytest.fixture
def jack_with_3_active_accounts():
    customer = Customer("1", "jack bauer")
    customer.add_account(Account("tr1", 10_000, AccountStatus.ACTIVE))
    customer.add_account(Account("tr2", 20_000, AccountStatus.ACTIVE))
    customer.add_account(Account("tr3", 30_000, AccountStatus.ACTIVE))
    return customer


@pytest.mark.parametrize("identity,fullname", customers)
def test_create_customer_is_successful(identity, fullname):
    customer = Customer(identity, fullname)
    assert customer.fullname == fullname
    assert customer.identity == identity
    assert len(customer.accounts) == 0

def test_get_account_should_success(jack_with_3_active_accounts):
    found_account = jack_with_3_active_accounts.get_account("tr1") # 2: call exercise method
    assert found_account is not None
    assert found_account.iban == "tr1"