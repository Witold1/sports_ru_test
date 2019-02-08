'''
Вынесенная отдельно функция для вывода статистик
'''


import numpy as np
from scipy.stats import mode


def print_stats(col):
    '''
    Принимает на вход численный признак-столбец.
    Возвращает отформатированную строку с нужными описательными статистиками признака.

    Для подсчета используются методы чистого numpy и scipy.stats.mode().
    Операции mode определена из scipy в области видимости скрипта.

    Example:

        print_stats(df[col].fillna(0))

    '''
    print(f'Для признака: {col.name}')

    str_out = \
    f'\tСреднее значение: {col.mean():.2f}.\n' +\
    f'\tМаксимальное / Минимальное значения: {col.max():.2f} / {col.min():.2f}.\n' +\
    f'\tМедиана: {col.median():.2f}.\n' + \
    f'\tМода: { {*mode(col).mode} }.\n'

    return str_out
