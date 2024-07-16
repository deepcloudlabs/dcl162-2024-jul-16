"""
CUT: Class Under Test -> Account
MUT: Method Under Test -> withdraw, deposit
                          __init__
                          __str__
                          getter
                          setter
Unit Test Phases:
1. Test Fixture/Setup
2. Call exercise method -> MUT
3. Verification
4. Teardown
"""
import pytest

from banking.account import Account, AccountStatus, InsufficientBalanceError

test_withdraw_failure_amount = [
    10_001, 10_000.001, 10_000.01, 10_000.10
]


@pytest.fixture
def an_active_account() -> Account:
    return Account("tr1", 10_000, AccountStatus.ACTIVE)


def test_withdraw_with_zero_amount_should_raise_exception(an_active_account):
    with pytest.raises(ValueError) as err:  # verification
        an_active_account.withdraw(0)  # 2. call exercise method
    # 4. teardown


@pytest.mark.parametrize('amount', test_withdraw_failure_amount)
def test_withdraw_with_over_balance_should_raise_exception(an_active_account,amount):
    with pytest.raises(InsufficientBalanceError) as err:  # verification
        an_active_account.withdraw(amount)  # 2. call exercise method
    # 4. teardown
