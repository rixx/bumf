from django.db import models


class CalculateTotal:

    @property
    def total(self):
        incoming = self.incoming_transactions\
            .aggregate(total=models.Sum('amount'))\
            .get('total') or 0
        outgoing = self.outgoing_transactions.\
            aggregate(total=models.Sum('amount'))\
            .get('total') or 0
        return incoming - outgoing
