import pytest

from bumf.core.models import Project


@pytest.mark.django_db
def test_project_str_contains_name(user):
    p = Project.objects.create(
        user=user,
        name='somename',
    )
    assert 'somename' in str(p)
    assert str(user) in str(p)


@pytest.mark.django_db
def test_project_str_contains_pk_if_no_name(user):
    p = Project.objects.create(
        user=user,
    )
    assert str(p.pk) in str(p)
    assert str(user) in str(p)
