from datetime import datetime
from django.utils import timezone


def parse_aware_datetime(dt_str: str, fmt: str = "%Y%m%d%H%M"):
    try:
        naive_dt = datetime.strptime(dt_str, fmt)
        return timezone.make_aware(naive_dt)
    except ValueError:
        raise ValueError(f"Invalid datetime format: {dt_str} (expected {fmt})")
