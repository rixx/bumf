from django.db import models


class Dossier(models.Model):
    """
    A dossier groups virtual transactions together. This replaces the concept
    of split transactions.
    """
    name = models.CharField(
        null=True, blank=True, max_length=60,
        verbose_name='Name',
        help_text='A dossier may be named to remember, search and find its contents',
    )
    project = models.ForeignKey(
        to='Project',
        on_delete=models.PROTECT,
        related_name='+',
    )


class VirtualTransaction(models.Model):
    """
    Virtual transactions track movement of money in virtual accounts, such as
    the budget category accounts, income and expense accounts.
    """
    dossier = models.ForeignKey(
        to='Dossier',
        on_delete=models.PROTECT,
        related_name='transactions',
        verbose_name='Transaction',
    )
    source = models.ForeignKey(
        to='VirtualAccount',
        on_delete=models.PROTECT,
        related_name='outgoing_transactions',
        verbose_name='Virtual account the money moves away from',
    )
    destination = models.ForeignKey(
        to='VirtualAccount',
        on_delete=models.PROTECT,
        related_name='incoming_transactions',
        verbose_name='Virtual account the money moves to',
    )
    bank_transaction = models.ForeignKey(
        to='RealTransaction', null=True, blank=True,
        on_delete=models.PROTECT,
        related_name='transactions',
        verbose_name='Bank transaction',
        help_text='The real-world bank transaction that describes this transaction.',
    )
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    comment = models.CharField(max_length=1000, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)


class RealTransaction(models.Model):
    """
    Real transactions move money around in the real world - such as bank
    transactions or paying your coffee in cash.
    """
    dossier = models.ForeignKey(
        to='Dossier',
        on_delete=models.PROTECT,
        related_name='bank_transactions',
        verbose_name='Bank transaction',
    )
    source = models.ForeignKey(
        to='RealAccount', null=True, blank=True,
        on_delete=models.PROTECT,
        related_name='outgoing_transactions',
        verbose_name='Account the money moves away from',
    )
    destination = models.ForeignKey(
        to='RealAccount', null=True, blank=True,
        on_delete=models.PROTECT,
        related_name='incoming_transactions',
        verbose_name='Account the money moves to',
    )
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    timestamp = models.DateTimeField(auto_now=True)
