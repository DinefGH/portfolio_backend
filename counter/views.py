from django.shortcuts import render

from django.http import JsonResponse
from .models import VisitCount
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .models import Visit
from django.db.models import F
from django.utils.timezone import localtime


@csrf_exempt
@api_view(['POST'])
def increment_visit(request):
    """
    Creates a new Visit instance to record the individual visit's timestamp.
    Updates the total visit count in the VisitCount model, increments by 1,
    and updates the last visit timestamp.
    Returns a JSON response containing the updated visit count and the timestamp of the visit.
    """

    visit = Visit.objects.create()

    visit_count, _ = VisitCount.objects.get_or_create(pk=1)
    visit_count.count = F('count') + 1
    visit_count.save()
    visit_count.refresh_from_db()
    visit_timestamp_str = localtime(visit.timestamp).isoformat()


    return Response({
        'message': 'Visit count incremented',
        'count': visit_count.count,
        'visit_timestamp': visit_timestamp_str,
    }, status=200)
