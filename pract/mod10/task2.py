import re
import doctest
import cProfile

# available_date = r'(d{1,2}[./-]d{1,2}[./-]d{2,4}|[А-Яа-я]+sd{1,2},sd{2,4}|[A-Za-z]+sd{1,2},sd{2,4}|[A-Za-z]{3}sd{1,2},sd{2,4}|d{2,4},s[A-Za-z]+sd{1,2}|d{2,4},s[A-Za-z]{3}sd{1,2})'
available_date = r'(\b\d{1,2}[./-]\d{1,2}[./-]\d{4}\b)|(\b\d{4}[./-]\d{1,2}[./-]\d{1,2}\b)|(\b\d{1,2}\s(?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)\s\d{4}\b)|(\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4}\b)|(\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{1,2},\s\d{4}\b)|(\b\d{4},\s(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2}\b)|(\b\d{4},\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{1,2}\b)'


def check_date(date):
    # if re.match(available_date, date):
    #     return True
    # else:
    #     return False
    if re.match(available_date, date, re.VERBOSE):
        # Проверка для февраля
        if re.search(r'(?:30|31)-(?:0?2|2)-\d{4}', date):
            return False
        # Проверка для месяца, где все месяцы имеют 30 дней
        if re.search(r'(?:31-(?:0?[469]|11))|(?:30-0?2)', date):
            return False
        return True
    else:
        return False


print(check_date("20 января 1806")) #T
print(check_date("1924, July 25")) #T
print(check_date("3.1.1506")) #T
print(check_date("26/09/1635")) #T
print('=' * 50)
print(check_date("25.08-1002")) #F
print(check_date("декабря 19, 1838")) #F
print(check_date("31 июня 2015")) #F
print(check_date("8.20.1973")) #F
print(check_date("Jun 7, -1563")) #F
print(check_date("31 февраля 2023")) #F

# def check(date):
#     """
#     :param date: Пример пароля
#     :return: Корректен ли введенный пароль?
#
#     >>> check("Abcdef12$")
#     True
#     >>> check("rtG&3FG#Tr^e")
#     True
#     >>> check("пароль")
#     False
#     """
#     if re.match(available_date, date):
#         return True
#     else:
#         return False
#
#
# if __name__ == "__main__":
#     doctest.testmod(verbose=True)
#     cProfile.run('check("rtG&3FG#Tr^e")')
