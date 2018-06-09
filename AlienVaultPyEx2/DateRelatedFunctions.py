# -*- coding: utf-8 -*-

""" File with some date manipulating functions """
from datetime import datetime

"""
This function receives a date in format string with isoformat Z
and converts it into date YYYY-MM-DD
"""


def DateDayConverter(StrDateInIsoformat):
    dt_time = datetime.strptime(StrDateInIsoformat, "%Y-%m-%dT%H:%M:%SZ")
    return dt_time.strftime("%Y-%m-%d")


"""
Implementation of the date conversion routine from PyGithub date
The import data type is datetime.datetime
"""


def DateConverterPyGithub(DateTimeFromPyGithub):
    return DateTimeFromPyGithub.strftime("%Y-%m-%dT%H:%M:%SZ")


""" """
