import pytest
from django.contrib.auth import get_user_model

from bumf.core.models import (
    Dossier, Project, ProjectScopeChoices, RealAccount,
    RealAccountVariants, RealTransaction, VirtualAccount,
    VirtualAccountVariants, VirtualTransaction,
)


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


@pytest.fixture
def project(user):
    return Project.objects.create(
        user=user,
        name='Some Test Project',
        default_budget_account=None,
        default_income_account=None,
        default_expense_account=None,
    )


@pytest.fixture
def business_project(project):
    project.scope = ProjectScopeChoices.BUSINESS
    project.save(update_fields=['scope'])
    return project


@pytest.fixture
def dossier(project):
    return Dossier.objects.create(
        name='Some Test Dossier',
        project=project,
    )


@pytest.fixture
def virtual_budget_account(project):
    return VirtualAccount.objects.create(
        name='Some Budget Account',
        variant=VirtualAccountVariants.BUDGET,
        project=project
    )


@pytest.fixture
def virtual_liability_account(project):
    return VirtualAccount.objects.create(
        name='Some Liability Account',
        variant=VirtualAccountVariants.LIABILITY,
        project=project
    )


@pytest.fixture
def virtual_income_account(project):
    return VirtualAccount.objects.create(
        name='Some Income Account',
        variant=VirtualAccountVariants.INCOME,
        project=project
    )


@pytest.fixture
def virtual_expense_account(project):
    return VirtualAccount.objects.create(
        name='Some Expense Account',
        variant=VirtualAccountVariants.EXPENSE,
        project=project
    )


@pytest.fixture
def bank_account(project):
    return RealAccount.objects.create(
        name='Some Bank Account',
        project=project,
        variant=RealAccountVariants.BANK_ACCOUNT,
    )


@pytest.fixture
def cash_account(project):
    return RealAccount.objects.create(
        name='Some Cash Account',
        project=project,
        variant=RealAccountVariants.CASH,
    )


@pytest.fixture
def bank_transaction(dossier, bank_account, cash_account):
    return RealTransaction.objects.create(
        dossier=dossier,
        source=bank_account,
        destination=cash_account,
        amount=10,
    )


@pytest.fixture
def virtual_transaction(dossier, virtual_budget_account, virtual_expense_account):
    return VirtualTransaction.objects.create(
        dossier=dossier,
        source=virtual_budget_account,
        destination=virtual_expense_account,
        amount=20,
    )
