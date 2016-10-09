from rates.models import Currency, Rate
from Queue import Queue
queue_rate = Queue()


def id_to_name(list_id):
    result = []
    for curr_id in list_id:
        result.append(Currency.objects.get(id=curr_id).name)
    return result


def getid_rate(curr_from, curr_to):
    result = Rate.objects.get(curr_from=curr_from, curr_to=curr_to)
    return result.value


def calc_prof(rate, id1, id2):
    result = rate * getid_rate(id1, id2)
    return result


def find_way_h(rate, id, way, ways):
    way = way[:]
    way.append(id)

    if calc_prof(rate, id, way[0]) > 1:
        way.append(way[0])
        rate = calc_prof(rate, id, way[0])
        ways.update({rate: way})
        return

    for r in Rate.objects.filter(curr_from=id):
        if id == r.curr_to.id:
            continue
        if r.curr_to.id in way:
            continue
        rate = calc_prof(rate, id, r.curr_to.id)
        queue_rate.put((rate, r.curr_to.id, way, ways))
        # print('queue_rate: %s' % queue_rate.queue)


def profit():
    currs_id = [curr.id for curr in Currency.objects.all()]
    ways = {}
    for id1 in currs_id:
        for curr2 in Rate.objects.filter(curr_from=id1):
            if id1 == curr2.curr_to.id:
                continue
            rate = getid_rate(id1, curr2.curr_to.id)
            find_way_h(rate, curr2.curr_to.id, [id1], ways)
    while ways == {}:
        find_way_h(*queue_rate.get())
    # print('ways: %s' % ways)
    return ways
