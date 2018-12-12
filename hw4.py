from datetime import datetime
from datetime import timedelta

#Задание 1
#Напишите функцию date_range, которая возвращает список дней между датами start_date и end_date.
#Даты должны вводиться в формате YYYY-MM-DD.
def data_range(start_date,end_date):
    start_date_dt=datetime.strptime(start_date,"%Y-%m-%d")
    end_date_dt = datetime.strptime(end_date, "%Y-%m-%d")
    temp_list=[]
    while start_date_dt<=end_date_dt:
        temp_list.append(start_date_dt.strftime("%Y-%m-%d"))
        start_date_dt+=timedelta(days=+1)
    return  temp_list

print(data_range("2018-01-01","2018-01-30"))


#Задание 2
#Дополните функцию из первого задания проверкой на корректность дат.
# В случае неверного формата или если start_date > end_date должен возвращаться пустой список.

def data_range(start_date,end_date):
    if start_date>end_date:
        return []
    else:
        start_date_dt = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_dt = datetime.strptime(end_date, "%Y-%m-%d")
        temp_list=[]
        while start_date_dt<=end_date_dt:
            temp_list.append(start_date_dt.strftime("%Y-%m-%d"))
            start_date_dt+=timedelta(days=+1)
        return temp_list

print(data_range("2018-01-30","2018-01-01"))



#Задание 3
#Дан поток дат в формате YYYY-MM-DD, в которых встречаются некорректные значения:
stream = ['2018-04-02', '2018-02-29', '2018-19-02']
#Напишите функцию, которая проверяет эти даты на корректность. Т. е. для каждой даты возвращает True (дата корректна) или
# False (некорректная дата).
def chef_dates(list_dates):
    dates_res=[]
    for i in list_dates:
        try:
            datetime.strptime(i,"%Y-%m-%d")
            dates_res.append("True")
        except ValueError:
            dates_res.append("False")
    return dates_res

print(chef_dates(stream))

#Задание 4
#Напишите функцию, которая возвращает список дат с 1 по вчерашний день текущего месяца.
# Если дан 1 день месяца, то возвращается список дней прошлого месяца.

def prev_dates():
    current_date=datetime.strptime('2018-01-01',"%Y-%m-%d")
    #current_date=datetime.today()
    date_list=[]
    if current_date.day!=1:
        first_day=current_date.replace(day=1)
        while first_day<current_date:
            date_list.append(first_day.strftime("%Y-%m-%d"))
            first_day+=timedelta(days=1)
        return date_list
    else:
        if current_date.month-1==0:
            first_day = current_date.replace(day=1,month=12)
            while first_day.month!=2:
                date_list.append(first_day.strftime("%Y-%m-%d"))
                first_day+=timedelta(days=1)
        else:
            first_day = current_date.replace(day=1, month=current_date.month-1)
            while first_day.month<current_date.month:
                date_list.append(first_day.strftime("%Y-%m-%d"))
                first_day+=timedelta(days=1)
        return date_list

print(prev_dates())






#Задание 5
#Напишите функцию, которая возвращает точную дату в формате YYYY-MM-DD по фразе:
#1. 'today' - сегодняшнюю дату
#2. 'last monday' -  прошлый понедельник
#3. 'last day' - Последний день текущего месяца

def get_day(command):
    today_date = datetime.today()
    if command=='today':
        return today_date.strftime("%Y-%m-%d")
    elif command=='last monday':
        day=today_date.weekday()
        while day!=0:
            day-=1
            today_date-=timedelta(days=1)
        return today_date.strftime("%Y-%m-%d")
    elif command=='last day':
        month_today_date=today_date.month
        new_month=month_today_date
        while month_today_date==new_month:
            today_date+=timedelta(days=1)
            new_month=today_date.month
        today_date-=timedelta(days=1)
        return today_date.strftime("%Y-%m-%d")
print(get_day('last day'))


# Задание 6
# Напишите функцию, которая разбивает на недели с понедельника по воскресенье интервал дат между start_date и end_date.
# Считайте, что входные данные всегда корректны. В ответ должны входить только полные недели.

from datetime import datetime
from datetime import timedelta


def divide_by_week(start_date, end_date):
    start_date_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_date_dt = datetime.strptime(end_date, "%Y-%m-%d")
    while start_date_dt.weekday() != 0:
        start_date_dt += timedelta(days=1)
    while end_date_dt.weekday() != 6:
        end_date_dt -= timedelta(days=1)
    range_weeks = []

    while start_date_dt < end_date_dt:
        range_weeks.append([start_date_dt.strftime("%Y-%m-%d"),(start_date_dt+timedelta(days=6)).strftime("%Y-%m-%d")])
        start_date_dt += timedelta(days=7)
    return range_weeks

print(divide_by_week("2019-01-01", "2019-01-31"))
