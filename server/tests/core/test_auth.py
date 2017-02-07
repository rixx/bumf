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


def test_user_string_without_mail():
    from django.contrib.auth import authenticate, get_user_model
    User = get_user_model()
    u = User(
        nick='nick',
    )
    assert str(u) == 'nick'


def test_user_string_with_mail():
    from django.contrib.auth import authenticate, get_user_model
    User = get_user_model()
    u = User(
        nick='nick',
        email='some@another.tld',
    )
    assert str(u) == 'nick (some@another.tld)'


def test_name_with_first_name():
    from django.contrib.auth import authenticate, get_user_model
    User = get_user_model()
    u = User(
        nick='nick',
        first_name='Nick!',
        email='some@another.tld',
    )
    assert u.get_full_name() == 'Nick!'
    assert u.get_short_name() == 'Nick!'


def test_name_without_first_name():
    from django.contrib.auth import authenticate, get_user_model
    User = get_user_model()
    u = User(
        nick='nick',
        email='some@another.tld',
    )
    assert u.get_full_name() == 'nick'
    assert u.get_short_name() == 'nick'
