import re
import doctest
import cProfile

available_password = r'^(?=.*[a-z].*[a-z])(?=.*\d)(?=.*[^,.!?]{3})[A-Za-z0-9^$%@#&*]{8,}$'


def checking_password(password):
    if re.match(available_password, password):
        return True
    else:
        return False


def check(password):
    """
    :param password: Пример пароля
    :return: Корректен ли введенный пароль?

    >>> check("Abcdef12$")
    True
    >>> check("rtG&3FG#Tr^e")
    True
    >>> check("пароль")
    False
    """
    if re.match(available_password, password):
        return True
    else:
        return False


if __name__ == "__main__":
    doctest.testmod(verbose=True)
    cProfile.run('check("rtG&3FG#Tr^e")')
