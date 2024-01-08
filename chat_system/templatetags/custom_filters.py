from django import template
from django.utils import timezone

register = template.Library()


@register.filter
def calculate_time_ago(last_message_timestamp):
    current_datetime = timezone.now()
    time_diff = current_datetime - last_message_timestamp

    time_d = time_diff.days
    time_m = time_diff.seconds // 60
    time_h = time_diff.seconds // 3600

    if time_d == 1:
        time_ago = f"{time_d} day ago"
    elif time_d > 0:
        time_ago = f"{time_d} days ago"
    elif time_m == 1:
        time_ago = f"{time_m} minute ago"
    elif 0 < time_m < 59:
        time_ago = f"{time_m} minutes ago"
    elif time_h == 1:
        time_ago = f"{time_h} hour ago"
    elif 0 < time_h < 59:
        time_ago = f"{time_h} hours ago"
    else:
        time_ago = "Just now"

    return time_ago
