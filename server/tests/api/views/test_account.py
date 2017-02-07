import pytest


@pytest.mark.django_db
def test_virtual_account_view(logged_in_client, virtual_income_account):
    response = logged_in_client.get('/v1/virtual-accounts/')
    assert len(response.data) == 1
