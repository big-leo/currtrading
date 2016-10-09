# from __future__ import unicode_literals
from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=3, unique=True)

    def rates(self):
        result = Rate.objects.filter(curr_from=self.pk)
        result = ','.join([rate.str_to() for rate in result])
        return result

    def __str__(self):
        result = '{\n %s}' % (self.rates())
        return result


class Rate(models.Model):
    curr_from = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='rate_curr_from', db_index=True)
    curr_to = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='rate_curr_to', db_index=True)
    value = models.FloatField()

    def __str__(self):
        return ('%s:%s->%.2f') % (self.curr_from.name, self.curr_to.name, self.value)

    def str_to(self):
        return ('\"%s\": %.2f') % (self.curr_to.name, self.value)

