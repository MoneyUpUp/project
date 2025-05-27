from django.utils import timezone
from datetime import timedelta
from products.models.update_tracker import LastUpdated


def should_update(name: str, minutes: int = 5) -> bool:
    now = timezone.now()
    try:
        tracker = LastUpdated.objects.get(name=name)
        return now - tracker.updated_at > timedelta(minutes=minutes)
    except LastUpdated.DoesNotExist:
        return True


def mark_updated(name: str):
    LastUpdated.objects.update_or_create(
        name=name, defaults={"updated_at": timezone.now()}
    )
