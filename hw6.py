import pandas as pd
pd.set_option('display.expand_frame_repr', False)
#Задание 1
#Используем файл keywords.csv.
#Необходимо написать гео-классификатор, который каждой строке сможет выставить географическую принадлежность определенному региону.
# Т. е. если поисковый запрос содержит название города региона, то в столбце 'region' пишется название этого региона.
# Если поисковый запрос не содержит названия города, то ставим 'undefined'.
#Правила распределения по регионам Центр, Северо-Запад и Дальний Восток:
#Результат классификации запишите в отдельный столбец region.

keywords=pd.read_csv('keywords.csv')

def get_region(row):
    geo_data = {
        'Центр': ['москва', 'тула', 'ярославль'],
        'Северо-Запад': ['петербург', 'псков', 'мурманск'],
        'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
    }

    for i in row['keyword'].split(' '):
        for key,value in geo_data.items():
            if i.lower() in value:
                return key
    return 'undefined'

keywords['region']=keywords.apply(get_region,axis=1)


#Задание 2
#Напишите функцию, которая классифицирует фильмы из материалов занятия по следующим правилам:
#    - оценка 2 и меньше - низкий рейтинг
#    - оценка 4 и меньше - средний рейтинг
#    - оценка 4.5 и 5 - высокий рейтинг
#Результат классификации запишите в столбец class
ratings=pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')
ratings['avg_rate']=ratings.groupby('movieId')['rating'].transform('mean')

def movie_classifier(row):
    if row['avg_rate']<=2:
        return 'низкий рейтинг'
    elif row['avg_rate']>2 and row['avg_rate']<=4:
        return 'средний рейтинг'
    else:
        return 'высокий рейтинг'

ratings['class']=ratings.apply(movie_classifier,axis=1)
final=ratings[['movieId','class']].merge(movies[['movieId','title']], on='movieId',how='left')
final.drop_duplicates(subset = 'movieId', keep = 'first', inplace = True)
print(final.head())
print()
#Задание 3
#Посчитайте среднее значение Lifetime киноманов (пользователи, которые поставили 100 и более рейтингов).
# Под Lifetime понимается разница между максимальным и минимальным значением timestamp для каждого пользователя. Ответ дайте в днях.
user_rates= ratings[['userId', 'rating']].groupby('userId').count().reset_index()
film_fans = user_rates[user_rates['rating']>100]['userId'].tolist()

lifetime=ratings[ratings['userId'].isin(film_fans)].groupby('userId').agg(['min','max'])['timestamp'].reset_index()
lifetime['diff']=lifetime['max']-lifetime['min']
print('Lifetime={:.2f}'.format(lifetime['diff'].mean()))
print()

#Задание 4
#Есть мнение, что "раньше снимали настоящее кино, не то что сейчас".
# Ваша задача проверить это утверждение, используя файлы с рейтингами фильмов из материалов занятия.
# Т. е. проверить верно ли, что с ростом года выпуска фильма его средний рейтинг становится ниже.
#При этом мы не будем затрагивать субьективные факторы выставления этих рейтингов, а пройдемся по следующему алгоритму:
#1. В переменную years запишите список из всех годов с 1950 по 2010.
#2. Напишите функцию production_year, которая каждой строке из названия фильма выставляет год выпуска.
# Не все названия фильмов содержат год выпуска в одинаковом формате, поэтому используйте следующий алгоритм:
#    - для каждой строки пройдите по всем годам списка years
#    - если номер года присутствует в названии фильма, то функция возвращает этот год как год выпуска
#    - если ни один из номеров года списка years не встретился в названии фильма, то возвращается 1900 год
#3. Запишите год выпуска фильма по алгоритму пункта 2 в новый столбец 'year'
#4. Посчитайте средний рейтинг всех фильмов для каждого значения столбца 'year' и отсортируйте результат по убыванию рейтинга

ratings=pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')
years=[str(i) for i in range(1950,2011)]
def production_year(row):
    for i in years:
        if i in row['title']:
            return i
    return '1900'
movies['year']=movies.apply(production_year,axis=1)
ratings_with_year=ratings.merge(movies[['year','movieId']],on='movieId',how='left')
print(ratings_with_year.groupby('year')['rating'].mean().reset_index().sort_values('rating',ascending=False))
