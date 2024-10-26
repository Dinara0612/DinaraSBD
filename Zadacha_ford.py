import time
import tracemalloc
from itertools import permutations

def Ford():
    # Определяем начало времени выполнения
    start_time = time.time()
    tracemalloc.start()
    
    D = 5  # Фиксируем D = 5, так как оно задано по условию
    
    # Перебираем возможные значения для O, исключая D
    for O in range(10):
        if O == D:
            continue

        # Перебираем уникальные цифры для остальных букв N, A, L, G, E, R, B, T
        remaining_digits = [i for i in range(10) if i not in {D, O}]
        for N, A, L, G, E, R, B, T in permutations(remaining_digits, 8):
            DONALD = D * 100000 + O * 10000 + N * 1000 + A * 100 + L * 10 + D
            GERALD = G * 100000 + E * 10000 + R * 1000 + A * 100 + L * 10 + D
            ROBERT = R * 100000 + O * 10000 + B * 1000 + E * 100 + R * 10 + T

            # Проверяем, выполняется ли уравнение
            if DONALD + GERALD == ROBERT:
                print(f"Есть решение: DONALD = {DONALD}, GERALD = {GERALD}, ROBERT = {ROBERT}")
                print(f"Ответ: D={D}, O={O}, N={N}, A={A}, L={L}, G={G}, E={E}, R={R}, B={B}, T={T}")
                
                # Получаем объем использования памяти
                current, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                
                # Определяем окончание времени выполнения
                end_time = time.time()
                
                # Выводим время выполнения и объем памяти
                print(f"Время выполнения: {end_time - start_time:.2f} секунд")
                print(f"Текущий объем памяти: {current / (1024 * 1024):.2f} МБ; Пиковый объем памяти: {peak / (1024 * 1024):.2f} МБ")
                return
    
    print("Нет решения")

Ford()
