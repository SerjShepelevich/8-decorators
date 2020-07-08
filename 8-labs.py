import time
import timeit
import os


#Создадим декоратор
#1. Написать декоратор, замеряющий время выполнение декорируемой функции.
def dec_f(f):
    def wrapper(*args, **kwargs):
        time_l = 0
        for i in range(100):
            time_1 = time.time()
            f(*args, **kwargs)
            elapsed_time = time.time() - time_1
            time_l += elapsed_time
        print("Среднее время выполнения функции:= ", str(time_l/100))
    return wrapper


#2. Сравнить время создания генератора и списка с элементами: натуральные числа от 1 до 1000000
#(создание объектов оформить в виде функций).

@dec_f
def list_n(num):
    list_of_num = []
    for i in range(num+1):
        list_of_num.append(i)
    return list_of_num

@dec_f
def list_g(num):
    for i in range(num+1):
        yield(i)


print('Функция создания списка')
list_n(1000000)

print('Генератор создания списка')
list_g(1000000)

#3. Написать декоратор, замеряющий объем оперативной памяти, потребляемый декорируемой функцией.
import psutil

def dec_size(f):
    def wrapper(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        print('Исп. память до вып. функции:' + str(proc.memory_info().rss / 1000000))
        f(*args, **kwargs)
        proc = psutil.Process(os.getpid())
        print('Исп. память после вып. функции:' + str(proc.memory_info().rss / 1000000))
    return wrapper

@dec_size
def list_n2(num):
    list_of_num = []
    for i in range(num+1):
        list_of_num.append(i)
    return list_of_num

@dec_size
def list_g2(num):
    for i in range(num+1):
        yield(i)

#4. Сравнить объем оперативной памяти для функции создания генератора и функции
# создания списка с элементами: натуральные числа от 1 до 1000000.

print("Работа функции создания листа")
list_n2(1000000)

print("Работа генератора создания листа")
list_g2(1000000)