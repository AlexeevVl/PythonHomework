import numpy as np
from numpy import linalg
import pandas as pd

#Задание 1
#Создайте numpy array с элементами от числа N до 0 (например, для N = 10 это будет array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])).
N=10
a = np.arange(N-1,-1,-1)
print(a)

#Задание 2
#Создайте диагональную матрицу с элементами от N до 0. Посчитайте сумму ее значений на диагонали.
mat_diag=np.diag(np.arange(N,-1,-1))
sum_diag_elements=np.trace(mat_diag)
print('Summa diag elements = {}'.format(sum_diag_elements))

#Задание 3
#Скачайте с сайта https://grouplens.org/datasets/movielens/ датасет любого размера. Определите какому
#фильму было выставлено больше всего оценок 5.0.
movies_csv = pd.read_csv('movies.csv')
ratings_csv = pd.read_csv('ratings.csv')
ratings_max=ratings_csv['movieId'][ratings_csv['rating']==5.0].value_counts().idxmax()
print('This film was rated the most times: {}'.format(movies_csv[(movies_csv['movieId']==ratings_max)]['title'].values[0]))
#Задание 4
#По данным файла power.csv посчитайте суммарное потребление стран Прибалтики (Латвия, Литва и Эстония) категорий 4, 12 и 21
#за период с 2005 по 2010 года. Не учитывайте в расчетах отрицательные значения quantity.
data = pd.read_csv('power.csv')
sample=data[ (data['country'].isin(['Estonia','Lithuania','Latvia'])) & (data['category'].isin(['4','12','21'])) & (data['year']>=2005)
& (data['year']<=2010) & (data['quantity']>0)]
print(sample['quantity'].sum())

#Задание 5
#Решите систему уравнений:
#4x + 2y + z = 4
#x + 3y = 12
#5y + 4z = -3
# коэффициенты при переменных в левой части уравнения
a = np.array([[4,2,1],[1,3,0],[0,5,4]])
# значения в правой части уравнения
b = np.array([4,12,-3])
x,y,z=linalg.solve(a,b)
print("x={:.3f} ,y={:.3f} ,z={:.3f} ".format(x,y,z))
#Проверка корректности решения СЛАУ
print(np.allclose(np.dot(a,linalg.solve(a,b)),b))