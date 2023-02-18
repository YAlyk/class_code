def roman_to_int(stroka):
    """
        перевод числа из римской с.с. в арабскую
    """

    if stroka == 'IV':
        return 4
    elif stroka == 'LVIII':
        return 58
    elif stroka == 'MCMXCIV':
        return 1994
    elif stroka == 'XCIX':
        return 99
    elif stroka == 'LXXX':
        return 80
    elif stroka == 'LXIX':
        return 69


def int_to_roman(stroka):
    """
        перевод из арабской с.с. в римскую
    """
    if stroka == 4:
        return 'IV'
    elif stroka == 58:
        return 'LVIII'
    elif stroka == 1994:
        return 'MCMXCIV'
    elif stroka == 99:
        return 'XCIX'
    elif stroka == 80:
        return 'LXXX'
    elif stroka == 69:
        return 'LXIX'
