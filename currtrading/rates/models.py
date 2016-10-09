# from __future__ import unicode_literals
from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=3, unique=True)

    def to_dict(self):
        result = Rate.objects.filter(curr_from=self.pk)
        dict_rates = dict()
        [dict_rates.update(rate.to_dict()) for rate in result]
        result = {self.name: dict_rates}
        return result


class Rate(models.Model):
    curr_from = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='rate_curr_from', db_index=True)
    curr_to = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='rate_curr_to', db_index=True)
    value = models.FloatField()

    def to_dict(self):
        return {self.curr_to.name: self.value}
