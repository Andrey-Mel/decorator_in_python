import time



#Пишем декоратор замера затраченного времени создания списка и генератора
def test_time(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        stop = time.time()
        print(f"Время на эту операцию затратилось: {stop - start}")
        return result
    return wrapper


@test_time
def list_num_nat():
    num_list = []
    for i in range(1, 1000000):
        num_list.append(i)
    return num_list

@test_time
def gen_num_nat():
    for num in range(1, 1000000):
        yield (num)
    return num

print('Время создания списка чисел от 1 до 1000000')
list_num_nat()


print('Время создания генератора чисел от 1 до 1000000')
gen_num_nat()


#---------Сравниваю объём памяти генератора и списка с помощью декоратора

import os
import psutil

#-- Пишу декоратор замера памяти
def test_memory(f):
    def wrapper(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        print(f'Использование памяти до выполнения функции: {str(proc.memory_info().rss/1000000)}')
        result_2 = f(*args, **kwargs)
        proc = psutil.Process(os.getpid())
        print(f'Замер памяти после работы функции: {str(proc.memory_info().rss/1000000)}')
        return result_2
    return wrapper

@test_memory
def list_num_nat():
    num_list = []
    for i in range(1, 1000000):
        num_list.append(i)
    return num_list

@test_memory
def gen_num_nat():
    for num in range(1, 1000000):
        yield (num)
    return num


print('Тест памяти списка')
list_num_nat()

print('Тест памяти генератора')
gen_num_nat()
