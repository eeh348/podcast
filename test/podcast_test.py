# podcast_test.py
import datetime as dt

from app.podcast import format_search

def test_format_search():
    # should create a correctly formated output:
    assert format_search("To be or not to be that is the question") == 'To%20be%20or%20not%20to%20be%20that%20is%20the%20question'

    # it should handle special characters:
    assert format_search("The top 1%") == 'The%20top%201%'

    # it should handle inputs without spaces
    assert format_search("Freakonomics") == 'Freakonomics'

from app.podcast import format_date

def test_format_date():
    # should create a correctly formated output:
    assert format_date(1562188380000) == 'Jul 03 2019'

    # should correctly display a date in the past:
    assert format_date(512169180000) == 'Mar 25 1986'

    # should correctly display a date in the future
    assert format_date(1585170780000) == 'Mar 25 2020'
    
from app.podcast import format_dur

def test_format_dur():
    # should round up:
    assert format_dur(40000) == 667

    # should create a correctly formated output:
    assert format_dur(1) == 0

    # should create a correctly formated output:
    assert format_dur(5000000) == 83333