from functools import partial

from django.core.exceptions import ValidationError
from django.db import models

from bumf.core.models.utils import Choices


class VirtualAccountVariantChoices(Choices):
    """
    There is one main virtual account type, the budget account, used for budget
    categories. And there are liabilities …
    There are two virtual account types. Budget accounts for money you have,
    and liability accounts for money you owe. Then there is your income …
    There are three virutal account types. Budget accounts and income accounts
    for money you have or receive, and liabilities for money you owe. And of
    course your expenses …

    Amongst our chief virtual account types are such things as:
     - Budget accounts, holding money the user has and wishes to spend on that
       budget category
     - Liability accounts for debts and open invoices. For private users this
       will mostly be one hidden/magic account.
     - Income accounts, for money the user receives from external sources
     - Expense accounts for money spent.
    """
    BUDGET = 'budget'
    LIABILITY = 'liability'
    INCOME = 'income'
    EXPENSE = 'expense'

    valid_choices = [
        BUDGET, LIABILITY, INCOME, EXPENSE,
    ]


def validate_variant(variant, value):
    if not value == variant:
        raise ValidationError(f'The object\'s variant is "{value}", but "{variant}" is required!')


validate_budget_account = partial(validate_variant, VirtualAccountVariantChoices.BUDGET)
validate_income_account = partial(validate_variant, VirtualAccountVariantChoices.INCOME)
validate_expense_account = partial(validate_variant, VirtualAccountVariantChoices.EXPENSE)


class VirtualAccount(models.Model):
    """
    Virtual Accounts are used to budget money for its intended use. They are
    the heart of bumf and are roughly equivalent to YNAB's categories.
    """
    name = models.CharField(
        max_length=120,
        verbose_name='Name',
    )
    variant = models.CharField(
        max_length=VirtualAccountVariantChoices.get_max_length(),
        default=VirtualAccountVariantChoices.BUDGET,
        choices=VirtualAccountVariantChoices.get_choices(),
    )
    project = models.ForeignKey(
        to='Project',
        on_delete=models.PROTECT,
        related_name='virtual_accounts',
    )
    parent = models.ForeignKey(
        to='VirtualAccount', null=True, blank=True,
        on_delete=models.PROTECT,
        related_name='child_accounts',
    )
    comment = models.CharField(
        max_length=1000, null=True, blank=True,
    )


class RealAccountVariantChoices(Choices):
    BANK_ACCOUNT = 'bank'
    CASH = 'cash'

    valid_choices = [
        BANK_ACCOUNT, CASH,
    ]


class RealAccount(models.Model):
    """
    Real accounts mirror actual bank accounts (or wallets, or other assets).
    """
    name = models.CharField(
        max_length=120,
        verbose_name='Name',
    )
    project = models.ForeignKey(
        to='Project',
        on_delete=models.PROTECT,
        related_name='real_accounts',
    )
    variant = models.CharField(
        max_length=RealAccountVariantChoices.get_max_length(),
        default=RealAccountVariantChoices.BANK_ACCOUNT,
        choices=RealAccountVariantChoices.get_choices(),
    )
    import_transactions = models.BooleanField(default=False)

    @property
    def total(self):
        incoming = self.incoming_transactions\
            .aggregate(total=models.Sum('amount'))\
            .get('total') or 0
        outgoing = self.outgoing_transactions.\
            aggregate(total=models.Sum('amount'))\
            .get('total') or 0
        return incoming - outgoing
