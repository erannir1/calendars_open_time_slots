import itertools
from dateutil import parser
import datetime as dt
from dateutil import tz


def range_diff(r1, r2):
    s1, e1 = r1
    s2, e2 = r2
    endpoints = sorted((s1, s2, e1, e2))
    result = []
    if endpoints[0] == s1 and endpoints[1] != s1:
        result.append((endpoints[0], endpoints[1]))
    if endpoints[3] == e1 and endpoints[2] != e1:
        result.append((endpoints[2], endpoints[3]))
    return result


def multi_range_diff(r1_list, r2_list):
    for r2 in r2_list:
        r1_list = list(itertools.chain(*[range_diff(r1, r2) for r1 in r1_list]))
    return r1_list


def convert_str_to_timestamp(date_string):
    date_timestamp = parser.parse(date_string)
    return date_timestamp


def day_start_and_end_time(date):
    day_start = dt.datetime(date.year, date.month, date.day, tzinfo=tz.tzutc())
    day_end = dt.datetime(date.year, date.month, date.day, hour=23,
                          minute=59, second=59, microsecond=0, tzinfo=tz.tzutc())
    return day_start, day_end


def convert_result_to_dict(result_list):
    result_list_of_dicts = []
    for i in result_list:
        range_dict = {
            "startTime": i[0].isoformat(),
            "endTime": i[1].isoformat()
        }
        result_list_of_dicts.append(range_dict)
    return result_list_of_dicts