"""Игра "Угадай число" 
Компьютер сам загадывает и сам угадывает"""

import numpy as np

def predict_number (number:int=1)-> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        : число попыток
    """
    count = 0
    while True:
        count+=1
        predict_number = np.random.randint(1,101)
        if predict_number==number:
            break
    return count
print(f"Количество попыток: {predict_number(10)}")

def score_game (random_predict)-> int:
    """За какое количество попыток в среднем за 1000 подходов угадывается число

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_lt = []
    np.random.seed(1)#устанавливаем сид для воспроизводимости
    random_array = np.random.randint(1,101,size=(1000))#Загадали список чисел
    for number in random_array:
        count_lt.append(random_predict(number))
    score = int(np.mean(count_lt))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток!")
    return score
#Запускаем код
score_game(predict_number)