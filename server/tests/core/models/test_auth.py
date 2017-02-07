import pytest
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


@pytest.mark.django_db
def test_user_creation():
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
    u = User(
        nick='nick',
    )
    assert str(u) == 'nick'


def test_user_string_with_mail():
    u = User(
        nick='nick',
        email='some@another.tld',
    )
    assert str(u) == 'nick (some@another.tld)'


def test_name_with_first_name():
    u = User(
        nick='nick',
        first_name='Nick!',
        email='some@another.tld',
    )
    assert u.get_full_name() == 'Nick!'
    assert u.get_short_name() == 'Nick!'


def test_name_without_first_name():
    u = User(
        nick='nick',
        email='some@another.tld',
    )
    assert u.get_full_name() == 'nick'
    assert u.get_short_name() == 'nick'


@pytest.mark.parametrize('nick', ('nick', 'Nicholas', 'N1ch0las', '-_'))
@pytest.mark.django_db
def test_nick_validation_valid(nick):
    u = User(
        nick=nick,
        password='some_password',
    )
    u.full_clean()


@pytest.mark.parametrize('nick', ('n', '-', '1'))
def test_nick_validation_short(nick):
    with pytest.raises(ValidationError) as excinfo:
        u = User(
            nick=nick,
            password='some_password',
        )
        u.full_clean()
    assert 'between 2 and 60' in str(excinfo)


@pytest.mark.parametrize('nick', ('n'*65, '-'*61, '1'*1000))
def test_nick_validation_long(nick):
    with pytest.raises(ValidationError) as excinfo:
        u = User(
            nick=nick,
            password='some_password',
        )
        u.full_clean()
    assert 'between 2 and 60' in str(excinfo)


@pytest.mark.parametrize('nick', ("'; DROP TABLE users;", '{name}', '1$()'))
def test_nick_validation_alphabet(nick):
    with pytest.raises(ValidationError) as excinfo:
        u = User(
            nick=nick,
            password='some_password',
        )
        u.full_clean()
    assert 'ascii letters' in str(excinfo)


@pytest.mark.django_db
def test_nick_validation_in_use():
    with pytest.raises(ValidationError) as excinfo:
        User.objects.create_user(
            nick='n1cholas',
            password='some_password',
        )
        u = User(
            nick='n1cholaS',
            password='some_password'
        )
        u.full_clean()
    assert 'in use' in str(excinfo)
