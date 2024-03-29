import datetime


def unix_time_to_yyyy_mm_dd(unix_time: float):
    dt_object = datetime.datetime.fromtimestamp(unix_time)
    return dt_object.strftime("%Y-%m-%d")
