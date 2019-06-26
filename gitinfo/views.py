from django.http import HttpResponse
import json
from datetime import datetime
from .utils import get_git_info


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial
    raise TypeError("Type not serializable")


def gitinfo(request):
    data = get_git_info()

    return HttpResponse(json.dumps(data, default=json_serial), content_type='application/json')
