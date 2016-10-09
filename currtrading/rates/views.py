from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from rates.models import Currency, Rate


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def currencies(request):
    result = get_list_or_404(Currency)
    result = ',<p>'.join([('\"%s\": %s' % (curr.name, curr.__str__())) for curr in result])
    return HttpResponse(result)


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
        return HttpResponse(result.__str__())
    elif request.method == 'DELETE':
        Currency.objects.get(name=curr).delete()
        return HttpResponse("DELETE currency: %s" % (curr,))


def sequence(request):
    return HttpResponse("sequence")
