import pytest


@pytest.mark.django_db
def test_budget_account_view(logged_in_client, virtual_budget_account):
    response = logged_in_client.get('/v1/budget-accounts/')
    assert len(response.data) == 1


@pytest.mark.django_db
def test_no_other_accounts_in_budget_account_view(logged_in_client, virtual_income_account):
    response = logged_in_client.get('/v1/budget-accounts/')
    assert len(response.data) == 0
