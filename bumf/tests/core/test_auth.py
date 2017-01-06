import pytest


@pytest.mark.django_db
def test_user_creation():
    from django.contrib.auth import authenticate, get_user_model
    User = get_user_model()
    u = User.objects.create_user(
        nick='some_nick',
        password='some_password'
    )

    assert not u.is_staff
    assert not u.is_superuser
    assert authenticate(
        username='some_nick',
        password='some_password'
    )
    assert not authenticate(
        username='some_nick',
        password='password'
    )


@pytest.mark.django_db
def test_user_creation_additional_data():
    from django.contrib.auth import authenticate, get_user_model
    User = get_user_model()
    u = User.objects.create_user(
        nick='some_nick',
        password='some_password',
        is_staff=True,
        first_name='Aname'
    )

    assert u.is_staff
    assert u.first_name == 'Aname'
    assert not u.is_superuser
    assert authenticate(
        username='some_nick',
        password='some_password'
    )


@pytest.mark.django_db
def test_superuser_creation():
    from django.contrib.auth import authenticate, get_user_model
    User = get_user_model()
    u = User.objects.create_superuser(
        nick='some_other_nick',
        password='some_password'
    )

    assert u.is_staff
    assert u.is_superuser
    assert authenticate(
        username='some_other_nick',
        password='some_password'
    )
