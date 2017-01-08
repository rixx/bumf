from django.conf import settings
from django.db import models

from bumf.core.models.account import (
    validate_budget_account, validate_expense_account, validate_income_account,
)
from bumf.core.models.utils import Choices


class ProjectScopeChoices(Choices):
    PRIVATE = 'private'
    BUSINESS = 'business'

    valid_choices = [PRIVATE, BUSINESS]


class Project(models.Model):
    """
    A project is, technically, a collection of accounts belonging to a user
    (or, later on probably: a group of users).
    Practically, most users will probably have only one project (for their
    personal finances) or at most two (one for their personal finances, one for
    their professional finances).
    """
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='projects',
        verbose_name='User',
        help_text='The project\'s owner',
    )
    name = models.CharField(
        null=True, blank=True, max_length=60,
        verbose_name='Name',
        help_text='Give your project a name if you have multiple projects!',
    )
    scope = models.CharField(
        max_length=10, default=ProjectScopeChoices.PRIVATE,
        choices=ProjectScopeChoices.get_choices(),
    )
    default_budget_account = models.ForeignKey(
        to='VirtualAccount', null=True, blank=True,
        related_name='+',
        validators=[validate_budget_account, ]
    )
    default_income_account = models.ForeignKey(
        to='VirtualAccount', null=True, blank=True,
        related_name='+',
        validators=[validate_income_account, ]
    )
    default_expense_account = models.ForeignKey(
        to='VirtualAccount', null=True, blank=True,
        related_name='+',
        validators=[validate_expense_account, ]
    )

    def __str__(self) -> str:
        if self.name:
            return f'Project {self.name} by {self.user}'
        return f'Project #{self.pk} by {self.user}'
