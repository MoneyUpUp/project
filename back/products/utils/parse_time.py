from datetime import datetime
from django.utils import timezone


def parse_aware_datetime(dt_str: str, fmt: str = "%Y%m%d%H%M"):

    return timezone.make_aware(datetime.strptime(dt_str, fmt))
