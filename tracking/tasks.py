# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.signals import task_success
from tracking.models import carrier_identify
from tracking.spider.ghn_spider import GHNSpider
from tracking.spider.vnpost_spider import VnpostSpider
from tracking.models import Carrier, Parcel, Event
from tracking.serializers import EventSerializer, ParcelSerializer, EventNestedSerializer


CARRIER_SPIDER = {
    'vnpost': 'VnpostSpider',
    'ghn': 'GHNSpider'
}

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def task_get_data_from_spider(parcel_id):
    carrier = carrier_identify(parcel_id)
    print carrier
    if carrier:
        spider = eval(CARRIER_SPIDER[carrier.slug_name])(parcel_id, carrier.slug_name)
    else:
        spider = eval('GHNSpider')(parcel_id, 'ghn')
    result = spider.normalize()

    print result

    # create or update parcel by parcel_id
    parcel = result.get('parcel')
    parcel_obj, _ = Parcel.objects.get_or_create(parcel_id=parcel.get('parcel_id'))
    serializer = ParcelSerializer(parcel_obj, data=parcel, partial=True)
    serializer.is_valid()
    serializer.validated_data
    serializer.save()

    # get carrier
    carrier = result.get('carrier')
    carrier_obj = Carrier.objects.get(slug_name=carrier.get('slug_name'))

    # get or update event
    events = result.get('events_details')
    event_obj_list = []
    for event in events:
        # can't use here because .data always valid and missing parcel
        # event_serializer = EventSerializer(data=event, partial=True)
        event_obj, _ = Event.objects.get_or_create(parcel=parcel_obj, carrier=carrier_obj, **event)
        event_obj_list.append(event_obj)
    events_serializer = EventNestedSerializer(event_obj_list, many=True)
    return events_serializer.data