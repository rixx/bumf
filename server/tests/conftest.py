import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def user():
    User = get_user_model()
    user = User.objects.create(
        nick='test_Nick',
        first_name='Nico',
    )
    user.set_password('testpassword')
    return user


@pytest.fixture
def superuser():
    User = get_user_model()
    user = User.objects.create(
        nick='test_supernick',
        first_name='SuperNico',
        is_superuser=True,
        is_staff=True,
    )
    user.set_password('testpassword')
    return user


@pytest.fixture
def logged_in_client(client, user):
    client.force_login(user)
    return client
