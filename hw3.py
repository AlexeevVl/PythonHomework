#Задание 1
#Дан список вида:
#Напишите функцию, которая возвращает сумму элементов на диагонали. Т. е. 13+32+23+35.
data = [
    [13, 25, 23, 34],
    [45, 32, 44, 47],
    [12, 33, 23, 95],
    [13, 53, 34, 35],
]

def sum_diag(matrix):
    sum=0
    for i in range(len(matrix)):
        sum+=matrix[i][i]
    return sum

print(sum_diag(data))


#Задание 2
#Дан список чисел, часть из которых имеют строковый тип или содержат буквы.
# Напишите функцию, которая возвращает сумму квадратов элементов, которые могут быть числами.
data = [1, '5', 'abc', 20, '2']

def sum_square(temp):
    sum=0
    for i in temp:
        if isinstance(i,(int,float)):
            sum+=i**2
        elif isinstance(i,str) and i.isdigit():
            sum+=int(i)**2
    return sum

print(sum_square(data))


#Задание 3
#Напишите функцию, которая возвращает название валюты (поле 'Name') с максимальным значением курса с помощью
# сервиса https://www.cbr-xml-daily.ru/daily_json.js

import requests

def max_currency_value():
        all_currencies_value={}
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        response = r.json()['Valute']
        for i in response:
            all_currencies_value[i]=response[i]['Value']
        max_currencies_value_name=max(all_currencies_value.keys(),key=(lambda x:all_currencies_value[x]))
        return response[max_currencies_value_name]['Name']

print(max_currency_value())

#Задание 4
#Последнее упражнение с занятия
#1. Добавьте в класс еще один формат, который возвращает название валюты (например, 'Евро').
#2. Добавьте в класс параметр diff (со значениями True или False), который в случае значения True
# в методах eur и usd будет возвращать не курс валюты, а изменение по сравнению в прошлым значением.

import requests


class Rate:
    def __init__(self, format='value',diff=False):
        self.format = format
        self.diff=diff


    def exchange_rates(self):
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']

    def make_format(self, currency):
        response = self.exchange_rates()

        if currency in response:
            if self.format == 'full':
                return response[currency]

            if self.format == 'value':
                if not self.diff:
                    return response[currency]['Value']
                else:
                    return response[currency]['Value']-response[currency]['Previous']

            if self.format=='currency_name':
                return response[currency]['Name']

        return 'Error'

    def eur(self):
        """Возвращает курс евро на сегодня в формате self.format если diff=False иначе именение"""
        return self.make_format('EUR')

    def usd(self):
        """Возвращает курс доллара на сегодня в формате self.format"""
        return self.make_format('USD')


print (Rate(format='currency_name').make_format('EUR'))
print ("Изменение по сравнению c прошлым значением {:.3f}".format(Rate(diff=True).eur()))

#Задание 5
#Напишите функцию, возвращающую сумму первых n чисел Фибоначчи
def fib(n):
    #Функция возращает n-ое число Фионаччи
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)

def sum_fib(n):
    summa=0
    for i in range(1,n+1):
        summa+=fib(i)
    return summa

print(sum_fib(6))


#Задание 6
#Напишите функцию, преобразующую произвольный список вида ['2018-01-01', 'yandex', 'cpc', 100]
# в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}
list=['2018-01-01', 'yandex', 'cpc', 100]

def li(temp):
    if len(temp)==2:
       return {temp[0]:temp[1]}
    elif len(temp)>2:
        return {temp[0]:li(temp[1:])}

print(li(list))