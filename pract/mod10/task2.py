import re
import doctest
import cProfile

available_date = r'(\b\d{1,2}[./-]\d{1,2}[./-]\d{4}\b)|(\b\d{4}[./-]\d{1,2}[./-]\d{1,2}\b)|(\b\d{1,2}\s(?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)\s\d{4}\b)|(\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4}\b)|(\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{1,2},\s\d{4}\b)|(\b\d{4},\s(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2}\b)|(\b\d{4},\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{1,2}\b)'


def check_date(date):
    if re.match(available_date, date, re.VERBOSE):
        if re.search(r'(?:30|31)-(?:0?2|2)-\d{4}', date):
            return False
        if re.search(r'(?:31-(?:0?[469]|11))|(?:30-0?2)', date):
            return False
        return True
    else:
        return False


def check(date):
    """
    :param date: Пример даты
    :return: Корректна ли введенная дата?

    >>> check("20 января 1806")
    True
    >>> check("1924, July 25")
    True
    >>> check("3.1.1506")
    True
    >>> check("26/09/1635")
    True
    >>> check("25.08-1002")
    False
    >>> check("декабря 19, 1838")
    False
    >>> check("31 июня 2015")
    False
    >>> check("8.20.1973")
    False
    >>> check("Jun 7, -1563")
    False
    >>> check("31 февраля 2023")
    False
    """
    if re.match(available_date, date, re.VERBOSE):
        if re.search(r'(?:30|31)-(?:0?2|2)-\d{4}', date):
            return False
        if re.search(r'(?:31-(?:0?[469]|11))|(?:30-0?2)', date):
            return False
        return True
    else:
        return False


if __name__ == "__main__":
    doctest.testmod(verbose=True)
    cProfile.run('check("1924, July 25")')
