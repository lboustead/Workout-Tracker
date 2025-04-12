from django import template

register = template.Library()

@register.filter
def duration_hms(value):
    try:
        # If it's a timedelta, convert to seconds
        total_seconds = int(value.total_seconds())
    except AttributeError:
        # Otherwise, assume it's already an int
        total_seconds = int(value)

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return f"{hours:02}:{minutes:02}:{seconds:02}"
