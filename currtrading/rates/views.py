from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from rates.models import Currency, Rate
from rates.utils import profit, id_to_name
import json


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def currencies(request):
    result = get_list_or_404(Currency)
    dict_curr = dict()
    [dict_curr.update(curr.to_dict()) for curr in result]
    return HttpResponse(json.dumps(dict_curr))


@csrf_exempt
def currency(request, curr, to=''):
    if request.method == 'PUT':
        curr_from = Currency.objects.get(name=curr)
        curr_to = Currency.objects.get(name=to)
        rate = request.GET.get('rate')
        try:
            curr_rate = Rate.objects.get(curr_from=curr_from, curr_to=curr_to)
            curr_rate.value = float(rate)
            curr_rate.save()
        except ObjectDoesNotExist:
            Rate(curr_from=curr_from, curr_to=curr_to, value=rate).save()
        return HttpResponse("PUT currency: %s %s" % (curr, to))
    elif request.method == 'POST':
        Currency(name=curr).save()
        return HttpResponse("POST currency: %s" % (curr,))
    elif request.method == 'GET':
        result = get_object_or_404(Currency, name=curr)
        return HttpResponse(json.dumps(result.to_dict()))
    elif request.method == 'DELETE':
        Currency.objects.get(name=curr).delete()
        return HttpResponse("DELETE currency: %s" % (curr,))


def sequence(request):
    prof = profit()
    prof_proc = None
    seq = None
    if len(prof) == 1:
        prof_proc = list(prof.keys())[0]
        seq = prof[prof_proc]
        seq = id_to_name(seq)
        result = {"profit_percent": prof_proc, "sequence": seq}
        return HttpResponse(json.dumps(result))
    else:
        result = 'no risk - free opportunities exist yielding over 1.00 % profit exist'
        return HttpResponse(result)

