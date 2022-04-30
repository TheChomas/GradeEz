from datetime import datetime, timedelta


def datetime_now_plus_minutes(minutes: int = 30):
    return datetime.now() + timedelta(minutes)
